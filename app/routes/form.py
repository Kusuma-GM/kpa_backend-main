from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from datetime import date

router = APIRouter(
    prefix="/api",
    tags=["Form"]
)

def convert_dates(obj):
    """Recursively convert all `date` objects to string for JSON serialization"""
    if isinstance(obj, dict):
        return {k: convert_dates(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_dates(i) for i in obj]
    elif isinstance(obj, date):
        return obj.isoformat()
    return obj


@router.post("/forms/wheel-specifications", response_model=schemas.WheelSpecResponse, status_code=201)
def create_wheel_spec(payload: schemas.WheelSpecCreate, db: Session = Depends(get_db)):
    new_entry = models.WheelSpecification(
        form_number=payload.formNumber,
        submitted_by=payload.submittedBy,
        submitted_date=payload.submittedDate,
        fields=payload.fields.dict()
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": new_entry.form_number,
            "submittedBy": new_entry.submitted_by,
            "submittedDate": new_entry.submitted_date.isoformat(),
            "status": "Saved"
        }
    }


@router.post("/forms/bogie-checksheet", response_model=schemas.BogieChecksheetResponse, status_code=201)
def create_bogie_checksheet(payload: schemas.BogieChecksheetCreate, db: Session = Depends(get_db)):
    bogie_details = convert_dates(payload.bogieDetails.dict())
    bogie_checksheet = convert_dates(payload.bogieChecksheet.dict())
    bmbc_checksheet = convert_dates(payload.bmbcChecksheet.dict())

    new_entry = models.BogieChecksheet(
        form_number=payload.formNumber,
        inspection_by=payload.inspectionBy,
        inspection_date=payload.inspectionDate,
        bogie_details=bogie_details,
        bogie_checksheet=bogie_checksheet,
        bmbc_checksheet=bmbc_checksheet
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return {
        "success": True,
        "message": "Bogie checksheet submitted successfully.",
        "data": {
            "formNumber": new_entry.form_number,
            "inspectionBy": new_entry.inspection_by,
            "inspectionDate": new_entry.inspection_date.isoformat(),
            "status": "Saved"
        }
    }
