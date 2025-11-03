from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.device import DeviceCreate, DeviceOut
from crud.device import create_device, get_devices, get_device

router = APIRouter()

@router.post("/devices", response_model=DeviceOut)
def create(device: DeviceCreate, db: Session = Depends(get_db)):
    return create_device(db, device)

@router.get("/devices", response_model=list[DeviceOut])
def read_all(db: Session = Depends(get_db)):
    return get_devices(db)

@router.get("/devices/{device_id}", response_model=DeviceOut)
def read_one(device_id: int, db: Session = Depends(get_db)):
    device = get_device(db, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

