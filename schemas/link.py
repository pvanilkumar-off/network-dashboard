from pydantic import BaseModel

class LinkCreate(BaseModel):
    name: str
    url: str
    device_id: int  # e.g., host, switch, router

class LinkOut(LinkCreate):
    id: int

    class Config:
        from_attributes = True  # or use from_attributes if you're on Pydantic v2
