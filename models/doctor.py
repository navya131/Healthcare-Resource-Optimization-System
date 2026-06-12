from dataclasses import asdict, dataclass


@dataclass
class Doctor:
    user_id: int
    specialization: str | None = None
    department: str | None = None
    experience: int | None = None
    qualification: str | None = None
    consultation_fee: float | None = None
    bio: str | None = None

    def to_dict(self):
        return asdict(self)
