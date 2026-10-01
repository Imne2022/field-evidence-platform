from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Source(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    domain: Mapped[str] = mapped_column(String(255))
    source_type: Mapped[str] = mapped_column(String(50), default="wordpress")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    posts: Mapped[list["Post"]] = relationship(back_populates="source")


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"))
    title: Mapped[str] = mapped_column(String(500))
    url: Mapped[str] = mapped_column(String(1000), unique=True)
    published_at: Mapped[datetime] = mapped_column(DateTime)
    raw_html: Mapped[str] = mapped_column(Text)
    extracted_text: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(50), default="raw")

    source: Mapped[Source] = relationship(back_populates="posts")
    candidate: Mapped["IncidentCandidate | None"] = relationship(
        back_populates="post", uselist=False
    )


class IncidentCandidate(Base):
    __tablename__ = "incident_candidates"

    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), unique=True)
    incident_type: Mapped[str] = mapped_column(String(50))
    confidence: Mapped[float] = mapped_column(Float, default=0.5)
    status: Mapped[str] = mapped_column(String(50), default="pending")

    post: Mapped[Post] = relationship(back_populates="candidate")