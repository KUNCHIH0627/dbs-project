@echo off
cd C:\Users\User\code\dbs\dbs-project\api
cd /d %~dp0api
call venv\Scripts\activate.bat
uvicorn app.main:app --host 0.0.0.0 --port 7777
pause