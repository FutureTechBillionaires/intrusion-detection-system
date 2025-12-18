from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class LogEntryCreate(BaseModel):
    ip_address: str
    endpoint: str
    http_method: str
    status_code: int
    user_agent: str
    response_time: float
    is_threat: bool = False
    threat_type: Optional[str] = None
    severity: Optional[str] = None


class LogEntryResponse(BaseModel):
    id: int
    timestamp: datetime
    ip_address: str
    endpoint: str
    http_method: str
    status_code: int
    is_threat: bool
    threat_type: Optional[str] = None

    class Config:
        from_attributes = True