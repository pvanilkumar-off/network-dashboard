from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.link import LinkCreate, LinkOut
from crud.link import create_link, get_links, get_link, delete_link

router = APIRouter()

@router.post("/links", response_model=LinkOut)
def create(link: LinkCreate, db: Session = Depends(get_db)):
    return create_link(db, link)

@router.get("/links", response_model=list[LinkOut])
def read_all(db: Session = Depends(get_db)):
    return get_links(db)

@router.get("/links/{link_id}", response_model=LinkOut)
def read_one(link_id: int, db: Session = Depends(get_db)):
    link = get_link(db, link_id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link

@router.delete("/links/{link_id}")
def delete(link_id: int, db: Session = Depends(get_db)):
    if not delete_link(db, link_id):
        raise HTTPException(status_code=404, detail="Link not found")
    return {"message": "Link deleted"}
