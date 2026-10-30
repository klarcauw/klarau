from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

app = FastAPI(
    title="Event Management API",
    description="API for managing events and registrations",
    version="1.0.0"
)

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =================================
# 1. GET ALL EVENTS
# =================================
@app.get("/events", response_model=list[schemas.EventResponse])
def read_events(db: Session = Depends(get_db)):
    return crud.get_events(db)


# =================================
# 2. ADD NEW EVENT
# =================================
@app.post("/events", response_model=schemas.EventResponse)
def add_event(
    event: schemas.EventCreate,
    db: Session = Depends(get_db)
):
    return crud.create_event(db, event)


# =================================
# 3. DELETE EVENT
# =================================
@app.delete("/events/{event_id}")
def remove_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = crud.delete_event(db, event_id)

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return {"message": "Event deleted successfully"}


# =================================
# 4. REGISTER FOR EVENT
# =================================
@app.post(
    "/events/{event_id}/register",
    response_model=schemas.RegistrationResponse
)
def register_event(
    event_id: int,
    registration: schemas.RegistrationCreate,
    db: Session = Depends(get_db)
):
    event = crud.get_event(db, event_id)

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return crud.create_registration(
        db,
        event_id,
        registration
    )


# =================================
# 5. GET EVENT REGISTRATIONS
# =================================
@app.get(
    "/events/{event_id}/registrations",
    response_model=list[schemas.RegistrationResponse]
)
def read_registrations(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = crud.get_event(db, event_id)

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return crud.get_registrations(db, event_id)