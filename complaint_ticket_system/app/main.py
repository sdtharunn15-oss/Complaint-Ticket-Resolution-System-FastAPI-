from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.complaints import router as complaints_router
from app.routers.tickets import router as tickets_router
from app.database import Base, engine
import app.models
from app.routers.users import router as users_router
from app.routers.reports import router as reports_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Complaint Ticket Resolution System",
    version="0.1.0"
)
Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(complaints_router)
app.include_router(tickets_router)
app.include_router(users_router)
app.include_router(reports_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {
        "message": "Complaint Ticket Resolution System API"
    }