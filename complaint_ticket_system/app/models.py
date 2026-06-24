from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

from sqlalchemy import DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="user")


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)

    category = Column(String)
    priority = Column(String)

    status = Column(String, default="Open")

    user_id = Column(Integer, ForeignKey("users.id"))


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    complaint_id = Column(Integer, ForeignKey("complaints.id"))
    agent_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending")
    resolution_notes = Column(Text, nullable=True)



class ResolutionHistory(Base):
    __tablename__ = "resolution_history"

    id = Column(Integer, primary_key=True, index=True)

    ticket_id = Column(Integer, ForeignKey("tickets.id"))

    resolution_note = Column(Text)

    resolved_by = Column(Integer)

    resolved_at = Column(
     DateTime,
        default=datetime.utcnow
    )