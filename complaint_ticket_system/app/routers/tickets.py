from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models import Ticket, ResolutionHistory
from app.schemas import (
    TicketCreate,
    TicketResponse,
    ResolutionCreate
)

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


# Create Ticket
@router.post("/", response_model=TicketResponse)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    new_ticket = Ticket(
        complaint_id=ticket.complaint_id,
        agent_id=ticket.agent_id,
        status="pending"
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


# Get All Tickets
@router.get("/", response_model=list[TicketResponse])
def get_tickets(
    status: Optional[str] = None,
    assigned_to: Optional[int] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(Ticket)

    if status:
        query = query.filter(
            Ticket.status == status
        )

    if assigned_to:
        query = query.filter(
            Ticket.agent_id == assigned_to
        )

    tickets = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return tickets

# Get Ticket By ID
@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


# Update Ticket
@router.put("/{ticket_id}")
def update_ticket(
    ticket_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    ticket.status = status

    db.commit()

    return {
        "message": "Ticket status updated"
    }


# Delete Ticket
@router.delete("/{ticket_id}")
def delete_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    db.delete(ticket)
    db.commit()

    return {
        "message": "Ticket deleted"
    }


# Assign Agent
@router.put("/{ticket_id}/assign")
def assign_ticket(
    ticket_id: int,
    agent_id: int,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    ticket.agent_id = agent_id

    db.commit()

    return {
        "message": "Agent assigned successfully"
    }


# Resolve Ticket
@router.put("/{ticket_id}/resolve")
def resolve_ticket(
    ticket_id: int,
    resolution_notes: str,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    ticket.status = "Resolved"
    ticket.resolution_notes = resolution_notes

    db.commit()

    return {
        "message": "Ticket resolved successfully"
    }


# Add Resolution History
@router.post("/{ticket_id}/resolution")
def create_resolution(
    ticket_id: int,
    resolution: ResolutionCreate,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    history = ResolutionHistory(
        ticket_id=ticket_id,
        resolution_note=resolution.resolution_note,
        resolved_by=1
    )

    db.add(history)

    ticket.status = "Resolved"

    db.commit()

    return {
        "message": "Resolution added successfully"
    }


# Get Resolution History
@router.get("/{ticket_id}/history")
def get_ticket_history(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    history = db.query(
        ResolutionHistory
    ).filter(
        ResolutionHistory.ticket_id == ticket_id
    ).all()

    return history