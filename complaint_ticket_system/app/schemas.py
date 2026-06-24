from pydantic import BaseModel


# User Schemas
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True


# Complaint Schemas
from typing import Literal

class ComplaintCreate(BaseModel):
    title: str
    description: str
    category: str
    priority: Literal[
        "Low",
        "Medium",
        "High",
        "Critical"
    ]


class ComplaintResponse(BaseModel):
    id: int
    title: str
    description: str

    category: str
    priority: str

    status: str
    user_id: int

    class Config:
        from_attributes = True
    


# Ticket Schemas
class TicketCreate(BaseModel):
    complaint_id: int
    agent_id: int


class TicketResponse(BaseModel):
    id: int
    complaint_id: int
    agent_id: int
    status: str
    resolution_notes: str | None = None

    class Config:
        from_attributes = True


# Resolution Schema
class ResolutionCreate(BaseModel):
    resolution_notes: str


    class ResolutionCreate(BaseModel):
     resolution_note: str


class ResolutionResponse(BaseModel):
    id: int
    ticket_id: int
    resolution_note: str
    resolved_by: int

    class Config:
        from_attributes = True

        class ResolutionCreate(BaseModel):
         resolution_note: str


