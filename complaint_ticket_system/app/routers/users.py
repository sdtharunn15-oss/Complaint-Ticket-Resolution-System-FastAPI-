from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, Ticket
from app.dependencies import admin_required

router = APIRouter(
    tags=["Users"]
)


@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return db.query(User).all()


@router.get("/agents")
def get_agents(
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return db.query(User).filter(
        User.role == "agent"
    ).all()


@router.get("/agents/{agent_id}/tickets")
def get_agent_tickets(
    agent_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return db.query(Ticket).filter(
        Ticket.agent_id == agent_id
    ).all()