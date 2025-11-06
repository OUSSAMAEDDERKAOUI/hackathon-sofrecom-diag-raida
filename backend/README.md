# Diag-Raida Backend API

Flask-based REST API for math diagnostic platform.

## Quick Start

### 1. Setup Environment

**Windows:**
```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python test_setup.py
```

**Linux/Mac:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 test_setup.py
```

### 2. Run the Server

**Windows:**
```cmd
start.bat
REM OR
venv\Scripts\activate
python run.py
```

**Linux/Mac:**
```bash
./start.sh
# OR
source venv/bin/activate
python3 run.py
```

Server will start at: `http://localhost:5000`

**⚠️ Important:** Always use the venv Python, NOT system Python!
- ✅ CORRECT: `source venv/bin/activate && python3 run.py`
- ❌ WRONG: `/usr/bin/python3 run.py` (will fail with ModuleNotFoundError)

### 3. Test the API
```bash
# Health check
curl http://localhost:5000/health

# Root endpoint
curl http://localhost:5000/

# Test analysis endpoint
curl -X POST http://localhost:5000/api/analysis/ \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

### 4. Run Tests
```bash
# Using pytest
pytest tests/

# Or using unittest
python -m unittest discover -s tests
```

## API Endpoints

### Health & Info
- `GET /health` - Health check
- `GET /` - API information

### Core Services
- `POST /api/analysis/` - Analyze diagnostic data
- `POST /api/evaluation/` - Evaluate student performance
- `POST /api/recommendation/` - Get personalized recommendations

## Project Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Flask app factory
│   ├── config.py            # Configuration
│   ├── routes/              # API endpoints
│   │   ├── analysis_routes.py
│   │   ├── evaluation_routes.py
│   │   └── recommendation_routes.py
│   ├── services/            # Business logic
│   │   ├── analysis_service.py
│   │   ├── evaluation_service.py
│   │   └── recommendation_service.py
│   ├── models/              # ML models
│   ├── data/                # JSON data files
│   └── utils/               # Helper functions
├── tests/                   # Test files
├── run.py                   # Entry point
└── requirements.txt         # Dependencies
```

## Current Status

✅ **Baseline (Ready for Main Branch)**
- Flask app structure with blueprints
- Configuration management
- Health check endpoints
- Basic route handlers
- Placeholder service implementations
- Basic tests

🚧 **In Development (Feature Branches)**
- ML model implementation
- Data loaders
- Full service logic
- LLM integration
- Comprehensive testing

## Development Workflow

See [docs/branching_strategy.md](../docs/branching_strategy.md) for Git workflow.

### Creating a Feature Branch
```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

### Team Member Assignments
1. **ML Models** → `feature/ml-models`
2. **Data Infrastructure** → `feature/data-infrastructure`
3. **Analysis/Evaluation** → `feature/analysis-evaluation`
4. **LLM/Recommendations** → `feature/llm-recommendations`
5. **Testing/Docs** → `feature/testing-docs`

## Environment Variables

Create a `.env` file (optional):
```bash
FLASK_ENV=development
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-key  # For LLM features
```

## Next Steps

1. ✅ Push baseline to `main`
2. Create `develop` branch
3. Team members create feature branches
4. Implement full services
5. Merge features to `develop`
6. Test integration
7. Merge to `main`

## Support

- Check documentation in `docs/`
- Review branching strategy before starting work
- Ask team before making major changes
