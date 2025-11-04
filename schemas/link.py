from pydantic import BaseModel

class LinkCreate(BaseModel):
    name: str
    url: str
    device_id: int  # e.g., host, switch, router

class LinkOut(BaseModel):
    id: int
    name: str
    url: str
    device_id: int

    class Config:
        orm_mode = True  # or use from_attributes if you're on Pydantic v2
