from sqlalchemy.orm import Session

from ..models.note import Note
from ..schemas.note import NoteCreate


def get_all(db: Session) -> list[Note]:
    """查全部筆記。"""
    return db.query(Note).all()


def get_by_id(db: Session, note_id: int) -> Note | None:
    """查指定 id 的筆記，找不到回傳 None。"""
    return db.query(Note).filter(Note.id == note_id).first()


def create(db: Session, note_data: NoteCreate) -> Note:
    """新增一筆筆記。"""
    db_note = Note(**note_data.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def update(db: Session, note: Note, note_data: NoteCreate) -> Note:
    """更新一筆已經查到的筆記。"""
    for key, value in note_data.model_dump().items():
        setattr(note, key, value)
    db.commit()
    db.refresh(note)
    return note


def delete(db: Session, note: Note) -> None:
    """刪除一筆已經查到的筆記。"""
    db.delete(note)
    db.commit()