from sqlalchemy.orm import Session
from models import Event, Registration
from schemas import EventCreate, RegistrationCreate


# Add new event
def create_event(db: Session, event: EventCreate):
    new_event = Event(**event.model_dump())

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event


# Show all events
def get_events(db: Session):
    return db.query(Event).order_by(Event.id.desc()).all()


# Get event by ID
def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()


# Delete event
def delete_event(db: Session, event_id: int):
    event = get_event(db, event_id)

    if event:
        db.delete(event)
        db.commit()

    return event


# Register event
def create_registration(
    db: Session,
    event_id: int,
    registration: RegistrationCreate
):
    new_registration = Registration(
        event_id=event_id,
        name=registration.name,
        phone=registration.phone
    )

    db.add(new_registration)
    db.commit()
    db.refresh(new_registration)

    return new_registration


# Show registrations
def get_registrations(db: Session, event_id: int):
    return db.query(Registration).filter(
        Registration.event_id == event_id
    ).all()