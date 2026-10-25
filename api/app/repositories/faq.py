from sqlalchemy.orm import Session

from app.models.faq import Faq
from app.schemas.faq import FaqCreate


def get_all(db: Session) -> list[Faq]:
    return db.query(Faq).order_by(Faq.id).all()


def get_by_id(db: Session, faq_id: int) -> Faq | None:
    return db.query(Faq).filter(Faq.id == faq_id).first()


def create(db: Session, faq_data: FaqCreate) -> Faq:
    faq = Faq(**faq_data.model_dump())
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq


def update(db: Session, faq: Faq, faq_data: FaqCreate) -> Faq:
    for field, value in faq_data.model_dump().items():
        setattr(faq, field, value)
    db.commit()
    db.refresh(faq)
    return faq


def delete(db: Session, faq: Faq) -> None:
    db.delete(faq)
    db.commit()