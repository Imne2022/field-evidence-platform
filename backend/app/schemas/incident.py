from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

IncidentType = Literal[
    "poisoning",
    "negligence",
    "data_breach",
    "wrongful_diagnosis",
    "unauthorized_procedure",
    "medical_privacy_violation",
]
IncidentStatus = Literal["reported", "alleged", "under_review", "documented", "closed"]
Severity = Literal["low", "medium", "high", "critical"]


class IncidentCreate(BaseModel):
    incident_code: str
    title: str
    incident_type: IncidentType
    severity: Severity = "medium"
    summary: str
    first_reported_at: datetime
    source_post_id: int | None = None


class IncidentRead(IncidentCreate):
    id: int
    status: IncidentStatus
    created_at: datetime

    class Config:
        from_attributes = True