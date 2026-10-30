from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from typing import Optional


# Create Event
class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    event_date: date


# Event Response
class EventResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    event_date: date
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# Create Registration
class RegistrationCreate(BaseModel):
    name: str
    phone: str


# Registration Response
class RegistrationResponse(BaseModel):
    id: int
    event_id: int
    name: str
    phone: str
    registered_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)