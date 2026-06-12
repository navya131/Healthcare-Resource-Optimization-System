from dataclasses import asdict, dataclass


@dataclass
class Appointment:
    patient_user_id: int
    doctor_id: int
    appointment_date: str
    appointment_time: str
    reason: str | None = None
    status: str = "Pending"
    cancellation_reason: str | None = None

    def to_dict(self):
        return asdict(self)
