from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

INCIDENT_STATUSES = ("reported", "alleged", "under_review", "documented", "closed")


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True)
    incident_code: Mapped[str] = mapped_column(String(50), unique=True)
    title: Mapped[str] = mapped_column(String(500))
    incident_type: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(50), default="reported")
    severity: Mapped[str] = mapped_column(String(20), default="medium")
    summary: Mapped[str] = mapped_column(Text)
    first_reported_at: Mapped[datetime] = mapped_column(DateTime)
    source_post_id: Mapped[int | None] = mapped_column(
        ForeignKey("posts.id"), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)