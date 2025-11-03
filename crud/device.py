from sqlalchemy.orm import Session
from models.device import Device
from schemas.device import DeviceCreate

def create_device(db: Session, device: DeviceCreate):
    db_device = Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_devices(db: Session):
    return db.query(Device).all()

def get_device(db: Session, device_id: int):
    return db.query(Device).filter(Device.id == device_id).first()
