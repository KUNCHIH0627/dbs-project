import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg

# 指向 api/.env 檔案路徑
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def get_connection():
    """建立並回傳一個資料庫連線。呼叫端用完要負責 conn.close()。"""
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("找不到 DATABASE_URL，請檢查 .env 檔案")
    return psycopg.connect(db_url)