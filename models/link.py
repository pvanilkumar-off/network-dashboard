from sqlalchemy import Column, Integer, String,ForeignKey
from db.base import Base
from sqlalchemy.orm import relationship


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url= Column(String, nullable=False)
    device_id= Column(Integer, ForeignKey("devices.id"))
    
    device=relationship("Devices",back_populates="links")

