import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg
from fastapi import APIRouter, HTTPException

# 指向 api/.env 檔案路徑
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.get("/db-test")
def db_test():
    db_url = os.getenv("DATABASE_URL")

    if not db_url:
        raise HTTPException(status_code=500, detail="找不到 DATABASE_URL，請檢查 .env 檔案")

    try:
        conn = psycopg.connect(db_url)
        dbname = conn.info.dbname
        conn.close()
        return {"status": "success", "dbname": dbname}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"連線失敗: {str(e)}")