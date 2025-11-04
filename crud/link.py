from sqlalchemy.orm import Session
from models.link import Link
from schemas.link import LinkCreate

def create_link(db: Session, link_data: LinkCreate):
    link = Link(**link_data.model_dump())
    db.add(link)
    db.commit()
    db.refresh(link)
    return link

def get_links(db: Session):
    return db.query(Link).all()

def get_link(db: Session, link_id: int):
    return db.query(Link).filter(Link.id == link_id).first()

def delete_link(db: Session, link_id: int):
    link = get_link(db, link_id)
    if link:
        db.delete(link)
        db.commit()
        return True
    return False
