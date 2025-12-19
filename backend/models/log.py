from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from datetime import datetime

from db.database import Base

class LogEntry(Base):
    __tablename__ = 'log_entries'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String, index=True)
    endpoint = Column(String)
    http_method = Column(String)
    status_code = Column(Integer)
    user_agent = Column(String)
    response_time = Column(Float)
    is_threat = Column(Boolean, default=False)
    threat_type = Column(String, nullable=True)
    severity = Column(String, nullable=True)
    
    
