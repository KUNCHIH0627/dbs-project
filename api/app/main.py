from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My Backend API")

# 定義 Pydantic 模型
class Item(BaseModel):
    name: str
    price: float

@app.get("/health")
def health_check():
    return {"status": "ok"}

# 練習 1: 新增 /version 端點
@app.get("/version")
def get_version():
    return {"version": "0.1.0"}

# 練習 2: 新增 POST /items 端點
@app.post("/items")
def create_item(item: Item):
    return item