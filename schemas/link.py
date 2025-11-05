from pydantic import BaseModel

class LinkCreate(BaseModel):
    name: str
    url: str
    device_id: int

class LinkOut(LinkCreate):
    id: int

    class Config:
        from_attributes = True
