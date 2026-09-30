from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..core.database import get_connection, get_db
from ..models.note import Note
from ..schemas.note import NoteCreate, NoteResponse

router = APIRouter()


@router.get("/ping")
def ping():
    return {"message": "pong"}


@router.get("/version")
def version():
    return {"version": "0.1.0"}


@router.post("/items")
def create_item(item: dict):
    return item


@router.get("/db-test")
def db_test():
    try:
        conn = get_connection()
        dbname = conn.info.dbname
        conn.close()
        return {"status": "success", "dbname": dbname}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"連線失敗: {str(e)}")


# ---- notes CRUD ----

@router.post("/notes", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


@router.get("/notes", response_model=list[NoteResponse])
def list_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()


@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note_data: NoteCreate, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    for key, value in note_data.model_dump().items():
        setattr(note, key, value)
    db.commit()
    db.refresh(note)
    return note


@router.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()