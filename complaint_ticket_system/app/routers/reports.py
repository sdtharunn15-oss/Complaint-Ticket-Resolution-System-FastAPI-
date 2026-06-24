from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Ticket

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/overdue-tickets")
def get_overdue_tickets(
    db: Session = Depends(get_db)
):
    tickets = db.query(Ticket).filter(
        Ticket.status != "Resolved"
    ).all()

    return tickets


@router.get("/sla-compliance")
def get_sla_compliance(
    db: Session = Depends(get_db)
):
    total = db.query(Ticket).count()

    resolved = db.query(Ticket).filter(
        Ticket.status == "Resolved"
    ).count()

    return {
        "total_tickets": total,
        "resolved_tickets": resolved,
        "compliance_percentage": (
            (resolved / total) * 100 if total > 0 else 0
        )
    }