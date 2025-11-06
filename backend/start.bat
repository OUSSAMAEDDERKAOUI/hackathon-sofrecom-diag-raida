@echo off
REM Quick start script for Windows - always uses venv Python

cd /d "%~dp0"

REM Check if venv exists
if not exist "venv\" (
    echo ❌ Virtual environment not found!
    echo Creating venv...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

echo ✅ Virtual environment activated
echo 🚀 Starting Diag-Raida API...
echo.

python run.py
