#!/usr/bin/env bash
set -e

echo "🧩 Setting up Diag-Raida environment (Linux/macOS)..."

# Create Python virtual environments
python3 -m venv backend/venv
python3 -m venv frontend/venv

# Activate backend venv and install dependencies
source backend/venv/bin/activate
echo "📦 Installing backend dependencies..."
pip install --upgrade pip
pip install -r backend/requirements.txt
deactivate

# Activate frontend venv and install dependencies
source frontend/venv/bin/activate
echo "📦 Installing frontend dependencies..."
pip install --upgrade pip
pip install -r frontend/requirements.txt
deactivate

# Run both services in the background
echo "🚀 Starting backend..."
(cd backend && source venv/bin/activate && python run.py &)

sleep 3
echo "🚀 Starting frontend..."
(cd frontend && source venv/bin/activate && streamlit run app.py --server.port=8501 &)

echo "✅ All systems running! Visit: http://localhost:8501"
