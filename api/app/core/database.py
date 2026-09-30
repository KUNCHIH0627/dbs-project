import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 指向 api/.env 檔案路徑
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    """給原本 psycopg 用的連線方式，保留給 db_test.py / db-test 端點使用。"""
    if not DATABASE_URL:
        raise RuntimeError("找不到 DATABASE_URL，請檢查 .env 檔案")
    return psycopg.connect(DATABASE_URL)


# ---- 以下是 SQLAlchemy 需要的設定 ----
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """FastAPI 用 Depends(get_db) 呼叫，每次請求給一個獨立的資料庫 Session，用完自動關閉。"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()