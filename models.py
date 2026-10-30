from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    TIMESTAMP,
    ForeignKey,
    text
)

from sqlalchemy.orm import relationship
from database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    event_date = Column(Date, nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

    registrations = relationship(
        "Registration",
        back_populates="event",
        passive_deletes=True
    )


class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(
        Integer,
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False
    )

    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)

    registered_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

    event = relationship(
        "Event",
        back_populates="registrations"
    )