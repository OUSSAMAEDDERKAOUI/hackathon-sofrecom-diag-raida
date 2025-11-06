# Quick Start Guide for Team Members

## 🚀 First Time Setup (5 minutes)

### 1. Clone and Navigate
```bash
git clone https://github.com/OUSSAMAEDDERKAOUI/hackathon-sofrecom-diag-raida.git
cd hackathon-sofrecom-diag-raida/backend
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Test Everything Works
```bash
# IMPORTANT: Make sure venv is activated!
# You should see (venv) in your prompt

# Run the server
python3 run.py

# OR use the helper script
./start.sh

# In another terminal, test the API
curl http://localhost:5000/health
```

**⚠️ Common Issue:** If you get `ModuleNotFoundError: No module named 'flask'`:
- You're using system Python instead of venv Python
- Solution: `source venv/bin/activate` first
- See `docs/IDE_SETUP.md` for IDE configuration

You should see:
```json
{
  "service": "Diag-Raida API",
  "status": "healthy",
  "version": "v1"
}
```

### 5. Run Tests
```bash
pytest tests/
```

All 6 tests should pass ✅

---

## 📋 Daily Workflow

### Starting Work
```bash
# 1. Activate virtual environment
cd backend
source venv/bin/activate

# 2. Pull latest changes
git checkout develop
git pull origin develop

# 3. Create/switch to your feature branch
git checkout -b feature/your-feature-name
# OR if branch exists:
git checkout feature/your-feature-name
git merge develop  # Stay updated
```

### During Development
```bash
# Run server (auto-reloads on changes)
python3 run.py

# Run tests frequently
pytest tests/

# Run specific test file
pytest tests/test_routes.py -v
```

### Ending Work
```bash
# 1. Commit your changes
git add .
git commit -m "feat: description of what you did"

# 2. Push to your branch
git push origin feature/your-feature-name

# 3. Create Pull Request on GitHub
# Target: feature/your-feature-name → develop
```

---

## 🎯 Team Member Assignments

### Member 1: ML Models
**Branch:** `feature/ml-models`

**Tasks:**
- Implement `backend/app/models/decision_tree_model.py`
- Create model training script
- Save trained models with joblib
- Add model evaluation metrics

**Files to work on:**
- `app/models/decision_tree_model.py`
- `app/models/train_model.py` (create new)
- `app/models/saved/` (directory for saved models)

### Member 2: Data Infrastructure
**Branch:** `feature/data-infrastructure`

**Tasks:**
- Implement `app/utils/data_loader.py`
- Create JSON schemas for questions and resources
- Populate `app/data/questions.json`
- Populate `app/data/resources.json`
- Add input validation helpers

**Files to work on:**
- `app/utils/data_loader.py`
- `app/utils/helpers.py`
- `app/data/questions.json`
- `app/data/resources.json`

### Member 3: Analysis & Evaluation Services
**Branch:** `feature/analysis-evaluation`

**Tasks:**
- Complete `app/services/analysis_service.py`
- Complete `app/services/evaluation_service.py`
- Integrate with ML models
- Add error handling and validation

**Files to work on:**
- `app/services/analysis_service.py`
- `app/services/evaluation_service.py`

### Member 4: LLM & Recommendations
**Branch:** `feature/llm-recommendations`

**Tasks:**
- Integrate OpenAI/Anthropic API
- Complete `app/services/recommendation_service.py`
- Design prompts for personalized suggestions
- Add LLM response caching (optional)

**Files to work on:**
- `app/services/recommendation_service.py`
- `app/utils/llm_client.py` (create new)

### Member 5: Testing & Documentation
**Branch:** `feature/testing-docs`

**Tasks:**
- Write comprehensive unit tests
- Write integration tests
- Create API documentation
- Add docstrings to all functions
- Create deployment guide

**Files to work on:**
- `tests/test_services.py`
- `tests/test_model.py`
- `docs/api_documentation.md` (create new)
- All existing files (add docstrings)

---

## 🔧 Useful Commands

### Git Commands
```bash
# See what changed
git status
git diff

# Undo uncommitted changes
git checkout -- filename

# See all branches
git branch -a

# Delete local branch
git branch -d feature/old-branch

# Update from develop
git checkout develop && git pull
git checkout feature/your-branch && git merge develop
```

### Python/Flask Commands
```bash
# Check Python version
python3 --version  # Should be 3.12

# Install new package
pip install package-name
pip freeze > requirements.txt  # Update requirements

# Run with different config
FLASK_ENV=production python3 run.py

# Python shell with app context
python3
>>> from app.main import create_app
>>> app = create_app()
>>> app.config
```

### Testing Commands
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test
pytest tests/test_routes.py::TestRoutes::test_health_check

# Run tests matching pattern
pytest -k "test_analysis"
```

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**This is the #1 most common issue!**

**Cause:** You're using system Python (`/usr/bin/python3`) instead of venv Python

**Solutions:**
```bash
# Solution 1: Activate venv (recommended)
cd backend
source venv/bin/activate  # You should see (venv) in prompt
python3 run.py

# Solution 2: Use helper script
cd backend
./start.sh

# Solution 3: Use venv Python directly
cd backend
./venv/bin/python3 run.py
```

**For IDE users:** See `docs/IDE_SETUP.md` to configure PyCharm/VS Code

### Issue: "Address already in use"
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

### "Import error" when running tests
```bash
# Make sure you're in backend directory
cd backend
pytest tests/
```

### Git merge conflicts
```bash
# Don't panic! Ask team for help
# Or follow conflict resolution in branching_strategy.md
```

---

## 📞 Communication

### Before You Start:
- Check team chat for updates
- Review branching strategy: `docs/branching_strategy.md`
- Coordinate with teammates on overlapping work

### While Working:
- Commit frequently with clear messages
- Push to your branch daily
- Update team on progress/blockers

### Before Merging:
- Test your code thoroughly
- Run all tests: `pytest tests/`
- Request code review from at least 1 teammate
- Resolve any merge conflicts

---

## ✅ Checklist for First Day

- [ ] Clone repository
- [ ] Create virtual environment
- [ ] Install dependencies
- [ ] Run server successfully
- [ ] Test API with curl
- [ ] Run tests (all pass)
- [ ] Read branching strategy
- [ ] Create your feature branch
- [ ] Make a small test commit
- [ ] Push to your branch
- [ ] Confirm you can see your branch on GitHub

---

## 📚 Additional Resources

- **Project Overview:** `docs/project_overview.md`
- **Branching Strategy:** `docs/branching_strategy.md`
- **Backend README:** `backend/README.md`
- **User Flow:** `docs/user_flow.md`

---

**Questions?** Ask in team chat! We're all learning together 🚀
