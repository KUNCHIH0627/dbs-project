import os
from pathlib import Path
from dotenv import load_dotenv

# 先載入 .env，確保 ROOT_PATH 等變數在建立 app 之前就緒
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.types import Scope
from starlette.exceptions import HTTPException

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    root_path=os.getenv("ROOT_PATH", ""),
)

# ---- API router，統一掛在 /api 底下 ----
from .api import router as api_router
app.include_router(api_router, prefix="/api")


# ---- 限制靜態檔案只公開 .html 和 .css ----
class RestrictedStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope: Scope):
        if path and not path.endswith("/"):
            if not (path.endswith(".html") or path.endswith(".css")):
                raise HTTPException(status_code=404)
        return await super().get_response(path, scope)


# ---- 靜態網站 root ----
public_directory = Path(__file__).resolve().parent / "public"
index_file = public_directory / "index.html"


@app.get("/", include_in_schema=False)
async def index():
    return FileResponse(index_file)


app.mount("/", RestrictedStaticFiles(directory=str(public_directory), html=True), name="static")