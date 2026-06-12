from dataclasses import asdict, dataclass


@dataclass
class Patient:
    user_id: int
    age: int | None = None
    gender: str | None = None
    weight: float | None = None
    height: float | None = None
    blood_group: str | None = None
    allergies: str | None = None
    medical_conditions: str | None = None
    family_history: str | None = None
    insurance_provider: str | None = None
    insurance_number: str | None = None

    def to_dict(self):
        return asdict(self)
