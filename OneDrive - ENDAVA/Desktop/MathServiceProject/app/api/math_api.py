
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.math_schemas import PowRequest, PowResponse, FibonacciRequest, FibonacciResponse, FactorialRequest, FactorialResponse, RequestLogSchema
from app.services.math_services import pow_operation, fibonacci_operation, factorial_operation
from app.db.database import SessionLocal
from app.models.request_log import RequestLog
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/pow", response_model=PowResponse)
def calculate_pow(request: PowRequest, db: Session = Depends(get_db)):
    try:
        result = pow_operation(request.base, request.exponent)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    log = RequestLog(
        operation="pow",
        input_data=json.dumps(request.dict()),
        result=str(result)
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return PowResponse(result=result)

@router.post("/fibonacci", response_model=FibonacciResponse)
def calculate_fibonacci(request: FibonacciRequest, db: Session = Depends(get_db)):
    try:
        result = fibonacci_operation(request.n)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    log = RequestLog(
        operation="fibonacci",
        input_data=json.dumps(request.dict()),
        result=str(result)
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return FibonacciResponse(result=result)

@router.post("/factorial", response_model=FactorialResponse)
def calculate_factorial(request: FactorialRequest, db: Session = Depends(get_db)):
    try:
        result = factorial_operation(request.n)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    log = RequestLog(
        operation="factorial",
        input_data=json.dumps(request.dict()),
        result=str(result)
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return FactorialResponse(result=result)


# Endpoint GET pentru log-uri
@router.get("/logs", response_model=list[RequestLogSchema])
def get_logs(db: Session = Depends(get_db)):
    logs = db.query(RequestLog).order_by(RequestLog.timestamp.desc()).all()
    return logs
