from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse
from app.security import hash_password, verify_password, create_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )


    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )


    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@router.post("/login")
def login(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == email
    ).first()


    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )


    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )


    token = create_token(
        {
            "user_id": user.id,
            "role": user.role
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }