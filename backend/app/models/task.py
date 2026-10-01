from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class EvidenceTask(Base):
    __tablename__ = "evidence_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    incident_id: Mapped[int] = mapped_column(ForeignKey("incidents.id"))
    task_type: Mapped[str] = mapped_column(String(50))
    zone_geohash: Mapped[str | None] = mapped_column(String(20), nullable=True)
    reward_amount: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(20), default="open")
    assigned_partner_id: Mapped[int | None] = mapped_column(
        ForeignKey("partners.id"), nullable=True
    )
    start_window: Mapped[datetime] = mapped_column(DateTime)
    end_window: Mapped[datetime] = mapped_column(DateTime)