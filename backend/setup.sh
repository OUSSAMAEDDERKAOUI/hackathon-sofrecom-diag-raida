#!/bin/bash
# Setup script for Diag-Raida backend

echo "🚀 Setting up Diag-Raida backend development environment..."

# Create a virtual environment
echo "🔧 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "🔄 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
    echo "ℹ️ Please edit the .env file with your OpenRouter API key"
else
    echo "ℹ️ .env file already exists"
fi

echo "✅ Setup complete!"
echo "🔹 Activate the virtual environment with: source venv/bin/activate"
echo "🔹 Run tests with: python -m pytest"
echo "🔹 Start the development server with: flask run"
