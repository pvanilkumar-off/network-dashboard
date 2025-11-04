from fastapi import FastAPI
from routers import device
from db.session import engine
from db.base import Base

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Network Dashboard API"}


# Include device routes
app.include_router(device.router)
