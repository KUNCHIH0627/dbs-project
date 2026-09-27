from .database import get_connection


def test_connection():
    try:
        conn = get_connection()
        print("連線成功:", conn.info.dbname)
        conn.close()
    except Exception as e:
        print("連線失敗:", e)


if __name__ == "__main__":
    test_connection()