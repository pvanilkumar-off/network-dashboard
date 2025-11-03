from sqlalchemy import Column, Integer, String
from db.base import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    ip_address = Column(String, unique=True)
    type = Column(String)  # e.g., host, switch, router
