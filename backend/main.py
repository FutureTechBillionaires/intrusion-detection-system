from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

from routers import log
from db.database import create_tables

create_tables()

app = FastAPI(
    title="AI-Powered Intrusion Detection System API",
    description="Backend API for real-time threat detection and monitoring",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "IDS Backend Running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(log.router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)






























'''
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="AI-Powered Intrusion Detection System API",
    description="Backend API for real-time threat detection and monitoring",
    version="1.0.0"
)

# Configure CORS - Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React development server
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)



# ROOT ENDPOINTS


@app.get("/")
def read_root():
    """Root endpoint - API information"""
    return {
        "message": "IDS Backend API is running",
        "version": "1.0.0",
        "status": "operational",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "database": "connected",
        "api": "operational"
    }



# LOG ENDPOINTS


@app.post("/api/logs", response_model=schemas.LogEntryResponse, status_code=201)
def create_log(log: schemas.LogEntryCreate, db: Session = Depends(get_db)):
    """
    Create a new log entry
    
    - **ip_address**: Source IP address
    - **endpoint**: API endpoint accessed
    - **http_method**: HTTP method (GET, POST, etc.)
    - **status_code**: HTTP status code
    - **user_agent**: Browser/client user agent
    - **response_time**: Response time in milliseconds
    """
    db_log = models.LogEntry(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


@app.get("/api/logs", response_model=List[schemas.LogEntryResponse])
def get_logs(
    skip: int = 0,
    limit: int = 100,
    threat_only: bool = False,
    db: Session = Depends(get_db)
):
    """
    Get all log entries
    
    - **skip**: Number of records to skip (pagination)
    - **limit**: Maximum number of records to return
    - **threat_only**: If true, return only threats
    """
    query = db.query(models.LogEntry)
    
    if threat_only:
        query = query.filter(models.LogEntry.is_threat == True)
    
    logs = query.order_by(models.LogEntry.timestamp.desc()).offset(skip).limit(limit).all()
    return logs


@app.get("/api/logs/{log_id}", response_model=schemas.LogEntryResponse)
def get_log(log_id: int, db: Session = Depends(get_db)):
    """Get a specific log entry by ID"""
    log = db.query(models.LogEntry).filter(models.LogEntry.id == log_id).first()
    
    if log is None:
        raise HTTPException(status_code=404, detail="Log entry not found")
    
    return log


@app.delete("/api/logs/{log_id}")
def delete_log(log_id: int, db: Session = Depends(get_db)):
    """Delete a specific log entry"""
    log = db.query(models.LogEntry).filter(models.LogEntry.id == log_id).first()
    
    if log is None:
        raise HTTPException(status_code=404, detail="Log entry not found")
    
    db.delete(log)
    db.commit()
    
    return {"message": "Log entry deleted successfully"}



# STATISTICS ENDPOINTS


@app.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    """
    Get overall statistics
    
    Returns:
    - Total number of logs
    - Number of threats detected
    - Number of normal logs
    - Threat percentage
    """
    total_logs = db.query(models.LogEntry).count()
    threat_logs = db.query(models.LogEntry).filter(models.LogEntry.is_threat == True).count()
    normal_logs = total_logs - threat_logs
    
    threat_percentage = round((threat_logs / total_logs * 100), 2) if total_logs > 0 else 0
    
    return {
        "total_logs": total_logs,
        "threats": threat_logs,
        "normal": normal_logs,
        "threat_percentage": threat_percentage
    }


@app.get("/api/stats/threats")
def get_threat_stats(db: Session = Depends(get_db)):
    """Get statistics broken down by threat type"""
    from sqlalchemy import func
    
    threat_breakdown = db.query(
        models.LogEntry.threat_type,
        models.LogEntry.severity,
        func.count(models.LogEntry.id).label('count')
    ).filter(
        models.LogEntry.is_threat == True
    ).group_by(
        models.LogEntry.threat_type,
        models.LogEntry.severity
    ).all()
    
    result = []
    for threat_type, severity, count in threat_breakdown:
        result.append({
            "threat_type": threat_type,
            "severity": severity,
            "count": count
        })
    
    return result


# SEARCH/FILTER ENDPOINTS


@app.get("/api/logs/search")
def search_logs(
    ip_address: Optional[str] = None,
    threat_type: Optional[str] = None,
    severity: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Search logs by various criteria
    
    - **ip_address**: Filter by IP address
    - **threat_type**: Filter by threat type
    - **severity**: Filter by severity level
    """
    query = db.query(models.LogEntry)
    
    if ip_address:
        query = query.filter(models.LogEntry.ip_address == ip_address)
    
    if threat_type:
        query = query.filter(models.LogEntry.threat_type == threat_type)
    
    if severity:
        query = query.filter(models.LogEntry.severity == severity)
    
    logs = query.order_by(models.LogEntry.timestamp.desc()).limit(100).all()
    
    return [schemas.LogEntryResponse.from_orm(log) for log in logs]


# STARTUP/SHUTDOWN EVENTS


@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    print("=" * 60)
    print(" IDS Backend API Starting...")
    print("=" * 60)
    print(" API Documentation: http://localhost:8000/docs")
    print(" Alternative docs: http://localhost:8000/redoc")
    print(" Health check: http://localhost:8000/health")
    print("=" * 60)


@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    print("👋 IDS Backend API shutting down...")


# ERROR HANDLERS

@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {
        "error": "Not Found",
        "message": "The requested resource was not found",
        "path": str(request.url)
    }


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return {
        "error": "Internal Server Error",
        "message": "An unexpected error occurred",
        "details": str(exc)
    }
    
    '''