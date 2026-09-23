import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg

# 強制指向 api/.env 檔案路徑
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

def test_connection():
    db_url = os.getenv("DATABASE_URL")
    
    if not db_url:
        print("錯誤：找不到 DATABASE_URL，請檢查 .env 檔案位置或內容！")
        return

    try:
        conn = psycopg.connect(db_url)
        print("連線成功:", conn.info.dbname)
        conn.close()
    except Exception as e:
        print("連線失敗:", e)

if __name__ == "__main__":
    test_connection()

