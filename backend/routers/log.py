from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from models.log import LogEntry
from schemas.log import LogEntryCreate, LogEntryResponse

router = APIRouter(
    prefix="/logs",
    tags=["logs"]
)

# this is to create a new log entry in the database
@router.post("/", response_model=LogEntryResponse)
def create_log(log: LogEntryCreate, db: Session = Depends(get_db)):
    db_log = LogEntry(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

# Now, to get all log entries from the database
@router.get("/", response_model=List[LogEntryResponse])
def get_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logs = db.query(LogEntry).offset(skip).limit(limit).all()
    return logs

@router.get("/{log_id}", response_model=LogEntryResponse)
def get_log(log_id: int, db: Session = Depends(get_db)):
    log = db.query(LogEntry).filter(LogEntry.id == log_id).first()
    
    if not log:
        raise HTTPException(status_code=404, detail="Log entry not found")
    
    return log