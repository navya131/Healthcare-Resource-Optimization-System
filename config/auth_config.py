import base64
import binascii
import hashlib
import hmac
import secrets

import streamlit as st

try:
    import bcrypt as _bcrypt
except ModuleNotFoundError:
    _bcrypt = None


_PBKDF2_PREFIX = "pbkdf2_sha256"
_PBKDF2_ITERATIONS = 390000


def hash_password(password):
    """
    Hash a password before storing in database.
    """
    if _bcrypt is not None:
        return _bcrypt.hashpw(
            password.encode("utf-8"),
            _bcrypt.gensalt()
        ).decode("utf-8")

    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        _PBKDF2_ITERATIONS,
    )
    return "{}${}${}${}".format(
        _PBKDF2_PREFIX,
        _PBKDF2_ITERATIONS,
        base64.b64encode(salt).decode("utf-8"),
        base64.b64encode(digest).decode("utf-8"),
    )


def verify_password(password, hashed_password):
    """
    Verify entered password against stored hash.
    """
    if hashed_password.startswith("$2") and _bcrypt is not None:
        return _bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )

    if hashed_password.startswith(f"{_PBKDF2_PREFIX}$"):
        try:
            _, iterations, salt_b64, digest_b64 = hashed_password.split("$", 3)
            expected = base64.b64decode(digest_b64.encode("utf-8"))
            salt = base64.b64decode(salt_b64.encode("utf-8"))
            derived = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                salt,
                int(iterations),
            )
            return hmac.compare_digest(derived, expected)
        except (ValueError, TypeError, binascii.Error):
            return False

    if _bcrypt is not None:
        return _bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )

    return False


def initialize_session():
    """
    Initialize session state variables.
    """
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user_id" not in st.session_state:
        st.session_state.user_id = None

    if "user_name" not in st.session_state:
        st.session_state.user_name = None

    if "user_role" not in st.session_state:
        st.session_state.user_role = None

    if "username" not in st.session_state:
        st.session_state.username = None

    if "role" not in st.session_state:
        st.session_state.role = None


def login_user(user_id, user_name, role):
    """
    Store logged-in user details.
    """
    normalized_role = "Admin" if role == "Hospital Staff" else role

    st.session_state.logged_in = True
    st.session_state.user_id = user_id
    st.session_state.user_name = user_name
    st.session_state.user_role = normalized_role
    st.session_state.username = user_name
    st.session_state.role = normalized_role


def logout_user():
    """
    Clear session data.
    """
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.user_name = None
    st.session_state.user_role = None
    st.session_state.username = None
    st.session_state.role = None


def is_authenticated():
    return st.session_state.get("logged_in", False)


def get_current_role():
    return st.session_state.get("user_role", None)
