Complaint & Ticket Resolution System

Objective

A FastAPI-based backend system for managing customer complaints, support tickets, agent assignments, and resolution tracking.


Tech Stack

- Python 3.9+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication


Features

Authentication
- User Registration
- User Login
- JWT Token Authentication

User & Agent Management
- Get All Users
- Get All Agents
- Get Agent Tickets

Complaint Management
- Create Complaint
- Get All Complaints
- Get Complaint By ID
- Update Complaint
- Delete Complaint

Ticket Management
- Create Ticket
- Get All Tickets
- Get Ticket By ID
- Update Ticket
- Delete Ticket
- Assign Ticket to Agent
- Resolve Ticket

Resolution Tracking
- Create Resolution
- View Ticket Resolution History

Reports
- Overdue Tickets Report
- SLA Compliance Report



Installation

Clone Repository

bash
git clone <repository-url>
cd complaint_ticket_system

Create Virtual Environment

bash
python -m venv venv


Activate Virtual Environment

Windows:

bash
venv\Scripts\activate


Install Dependencies

bash
pip install -r requirements.txt


Run Application

bash
uvicorn app.main:app --reload




API Documentation

Swagger UI:

text
http://127.0.0.1:8000/docs


OpenAPI JSON:

text
http://127.0.0.1:8000/openapi.json



Database Tables

- users
- complaints
- tickets
- resolution_history



Project Structure

text
complaint_ticket_system/
│
├── app/
│   ├── routers/
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── dependencies.py
│   ├── security.py
│   └── main.py
│
├── README.md
├── requirements.txt
└── database.db



Author

Tharun
