from pydantic import BaseModel

class DeviceCreate(BaseModel):
    name: str
    ip_address: str
    type: str  # e.g., host, switch, router

class DeviceOut(DeviceCreate):
    id: int
    
    class Config:
        from_attributes = True

