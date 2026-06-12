from dataclasses import asdict, dataclass


@dataclass
class DiseasePrediction:
    patient_user_id: int
    disease_type: str
    prediction: str
    risk_score: float
    severity: str

    def to_dict(self):
        return asdict(self)


@dataclass
class OutcomePrediction:
    patient_user_id: int
    recovery_probability: float
    icu_requirement: str
    mortality_risk: str
    expected_stay: int

    def to_dict(self):
        return asdict(self)
