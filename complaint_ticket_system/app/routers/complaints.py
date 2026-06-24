from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Complaint
from app.schemas import ComplaintCreate, ComplaintResponse
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)


# Create Complaint
@router.post("/", response_model=ComplaintResponse)
def create_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db)
):
    new_complaint = Complaint(
        title=complaint.title,
        description=complaint.description,
        category=complaint.category,
        priority=complaint.priority,
        user_id=1
    )

    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    return new_complaint


# Get All Complaints
@router.get("/", response_model=list[ComplaintResponse])
def get_complaints(
    db: Session = Depends(get_db)
):
    complaints = db.query(Complaint).all()
    return complaints


# Get Complaint By ID
@router.get("/{complaint_id}", response_model=ComplaintResponse)
def get_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):
    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not complaint:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint


# Update Complaint Status
@router.put("/{complaint_id}")
def update_complaint(
    complaint_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not complaint:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    complaint.status = status
    db.commit()

    return {
        "message": "Complaint updated"
    }


# Delete Complaint
@router.delete("/{complaint_id}")
def delete_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):
    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not complaint:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    db.delete(complaint)
    db.commit()

    return {
        "message": "Complaint deleted"
    }