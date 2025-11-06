@echo off
echo 🧩 Setting up Diag-Raida environment (Windows)...

REM --- Backend setup ---
cd backend
python -m venv venv
call venv\Scripts\activate
echo 📦 Installing backend dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
deactivate
cd ..

REM --- Frontend setup ---
cd frontend
python -m venv venv
call venv\Scripts\activate
echo 📦 Installing frontend dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
deactivate
cd ..

echo 🚀 Starting backend and frontend...

start cmd /k "cd backend && call venv\Scripts\activate && python run.py"
start cmd /k "cd frontend && call venv\Scripts\activate && streamlit run app.py --server.port=8501"

echo ✅ All systems running! Open http://localhost:8501
pause
