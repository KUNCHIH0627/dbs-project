from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..core.database import get_connection

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float


@router.get("/ping")
def ping():
    return {"message": "pong"}


@router.get("/version")
def version():
    return {"version": "0.1.0"}


@router.post("/items")
def create_item(item: Item):
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