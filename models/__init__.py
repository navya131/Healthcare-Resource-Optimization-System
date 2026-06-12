from models.appointment import Appointment
from models.doctor import Doctor
from models.ehr import MedicalRecord, Prescription
from models.patient import Patient
from models.reports import DiseasePrediction, OutcomePrediction
from models.resources import Resource

__all__ = [
    "Appointment",
    "DiseasePrediction",
    "Doctor",
    "MedicalRecord",
    "OutcomePrediction",
    "Patient",
    "Prescription",
    "Resource",
]
