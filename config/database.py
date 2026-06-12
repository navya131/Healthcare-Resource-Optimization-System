import sqlite3

DB_PATH = "database/healthcare.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _ensure_column(cursor, table_name, column_name, column_definition):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row["name"] for row in cursor.fetchall()]

    if column_name not in columns:
        cursor.execute(
            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_definition}"
        )


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    age INTEGER,
    gender TEXT,
    weight REAL,
    height REAL,
    blood_group TEXT,
    allergies TEXT,
    medical_conditions TEXT,
    family_history TEXT,
    insurance_provider TEXT,
    insurance_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors(
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    specialization TEXT,
    department TEXT,
    experience INTEGER,
    qualification TEXT,
    consultation_fee REAL,
    bio TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS doctor_schedules(
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER,
    available_date TEXT,
    start_time TEXT,
    end_time TEXT,
    max_patients INTEGER,
    FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_user_id INTEGER,
    doctor_id INTEGER,
    appointment_date TEXT,
    appointment_time TEXT,
    status TEXT DEFAULT 'Pending',
    reason TEXT,
    cancellation_reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(patient_user_id) REFERENCES users(id),
    FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
)
""")
    _ensure_column(cursor, "appointments", "cancellation_reason", "TEXT")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS medical_records(
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_user_id INTEGER,
    diagnosis TEXT,
    symptoms TEXT,
    treatment TEXT,
    doctor_notes TEXT,
    visit_date TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(patient_user_id) REFERENCES users(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS prescriptions(
    prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_user_id INTEGER,
    medication TEXT,
    dosage TEXT,
    duration TEXT,
    instructions TEXT,
    prescribed_date TEXT,
    FOREIGN KEY(patient_user_id) REFERENCES users(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS diagnostics(
    diagnostic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_user_id INTEGER,
    report_name TEXT,
    report_type TEXT,
    report_file TEXT,
    upload_date TEXT,
    FOREIGN KEY(patient_user_id) REFERENCES users(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS vaccinations(
    vaccine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_user_id INTEGER,
    vaccine_name TEXT,
    dose_number TEXT,
    vaccination_date TEXT,
    next_due_date TEXT,
    FOREIGN KEY(patient_user_id) REFERENCES users(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS beds(
    bed_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ward_type TEXT,
    bed_number TEXT UNIQUE,
    status TEXT DEFAULT 'Available',
    patient_user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")  
    cursor.execute("""
CREATE TABLE IF NOT EXISTS bed_forecasts(
    forecast_id INTEGER PRIMARY KEY AUTOINCREMENT,
    forecast_date TEXT,
    expected_requirement INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS staff(
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    department TEXT,
    contact_number TEXT,
    status TEXT DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS staff_shifts(
    shift_id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_id INTEGER,
    shift_date TEXT,
    shift_type TEXT,
    start_time TEXT,
    end_time TEXT,
    FOREIGN KEY(staff_id) REFERENCES staff(staff_id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS resources(
    resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_name TEXT,
    resource_type TEXT,
    quantity INTEGER,
    available_quantity INTEGER,
    status TEXT DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS resource_forecasts(
    forecast_id INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_type TEXT,
    predicted_demand INTEGER,
    forecast_date TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS report_analysis(
    analysis_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_user_id INTEGER,
    report_name TEXT,
    extracted_text TEXT,
    risk_level TEXT,
    findings TEXT,
    analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS disease_predictions(
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_user_id INTEGER,
    disease_type TEXT,
    prediction TEXT,
    risk_score REAL,
    severity TEXT,
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(patient_user_id) REFERENCES users(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS outcome_predictions(
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_user_id INTEGER,
    recovery_probability REAL,
    icu_requirement TEXT,
    mortality_risk TEXT,
    expected_stay INTEGER,
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(patient_user_id) REFERENCES users(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS emergency_alerts(
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_user_id INTEGER,
    alert_type TEXT,
    severity TEXT,
    message TEXT,
    status TEXT DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS chatbot_history(
    chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    user_message TEXT,
    bot_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS notifications(
    notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    channel TEXT,
    subject TEXT,
    message TEXT,
    status TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

    conn.commit()
    conn.close()
