from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.incident import Incident
from app.schemas.incident import IncidentCreate, IncidentRead

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post("", response_model=IncidentRead, status_code=201)
def create_incident(payload: IncidentCreate, db: Session = Depends(get_db)):
    incident = Incident(**payload.model_dump(), status="reported")
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return incident


@router.get("/{incident_code}", response_model=IncidentRead)
def get_incident(incident_code: str, db: Session = Depends(get_db)):
    incident = db.query(Incident).filter_by(incident_code=incident_code).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident