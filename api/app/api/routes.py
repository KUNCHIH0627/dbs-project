from fastapi import APIRouter, HTTPException
from ..core.database import get_connection

router = APIRouter()


@router.get("/ping")
def ping():
    return {"message": "pong"}


@router.get("/db-test")
def db_test():
    try:
        conn = get_connection()
        dbname = conn.info.dbname
        conn.close()
        return {"status": "success", "dbname": dbname}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"連線失敗: {str(e)}")