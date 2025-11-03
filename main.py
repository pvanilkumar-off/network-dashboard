from fastapi import FastAPI
from routers import device
from db.session import engine
from db.base import Base

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI()

# Include device routes
app.include_router(device.router)
