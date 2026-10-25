from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories import faq as faq_repo
from app.schemas.faq import FaqCreate, FaqResponse

router = APIRouter(prefix="/faqs", tags=["faqs"])


@router.post("", response_model=FaqResponse, status_code=status.HTTP_201_CREATED)
def create_faq(faq_data: FaqCreate, db: Session = Depends(get_db)):
    return faq_repo.create(db, faq_data)


@router.get("", response_model=List[FaqResponse])
def list_faqs(db: Session = Depends(get_db)):
    return faq_repo.get_all(db)


@router.get("/{faq_id}", response_model=FaqResponse)
def get_faq(faq_id: int, db: Session = Depends(get_db)):
    faq = faq_repo.get_by_id(db, faq_id)
    if faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return faq


@router.put("/{faq_id}", response_model=FaqResponse)
def update_faq(faq_id: int, faq_data: FaqCreate, db: Session = Depends(get_db)):
    faq = faq_repo.get_by_id(db, faq_id)
    if faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return faq_repo.update(db, faq, faq_data)


@router.delete("/{faq_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_faq(faq_id: int, db: Session = Depends(get_db)):
    faq = faq_repo.get_by_id(db, faq_id)
    if faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    faq_repo.delete(db, faq)