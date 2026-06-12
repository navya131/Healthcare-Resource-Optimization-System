from dataclasses import asdict, dataclass


@dataclass
class MedicalRecord:
    patient_user_id: int
    diagnosis: str
    symptoms: str
    treatment: str
    doctor_notes: str | None = None
    visit_date: str | None = None

    def to_dict(self):
        return asdict(self)


@dataclass
class Prescription:
    patient_user_id: int
    medication: str
    dosage: str
    duration: str
    instructions: str | None = None
    prescribed_date: str | None = None

    def to_dict(self):
        return asdict(self)
