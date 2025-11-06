# ⚡ Quick Reference Card

## 🚀 First Time Setup

### Windows
```cmd
git clone <repo-url>
cd hackathon-sofrecom-diag-raida\backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python test_setup.py
```

### Linux/Mac
```bash
git clone <repo-url>
cd hackathon-sofrecom-diag-raida/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 test_setup.py
```

---

## 🏃 Daily Commands

### Start App
**Windows:** `start.bat` or `python run.py`  
**Linux/Mac:** `./start.sh` or `python3 run.py`

### Run Tests
**All platforms:** `pytest tests/`

### Activate Venv
**Windows:** `venv\Scripts\activate`  
**Linux/Mac:** `source venv/bin/activate`

---

## 🔍 Test Everything Works

```bash
# 1. Health check
curl http://localhost:5000/health

# 2. Run tests
pytest tests/

# 3. Check setup
python test_setup.py
```

---

## 🌿 Git Workflow

```bash
# Start work
git checkout develop
git pull origin develop
git checkout -b feature/your-name

# During work
git add .
git commit -m "feat: what you did"
git push origin feature/your-name

# Update from develop
git checkout develop && git pull
git checkout feature/your-name
git merge develop
```

---

## 🐛 Quick Fixes

**"ModuleNotFoundError"**  
→ Activate venv first!

**"Address in use"**  
→ Windows: `netstat -ano | findstr :5000` then `taskkill /PID <PID> /F`  
→ Linux/Mac: `lsof -ti:5000 | xargs kill -9`

**"Permission denied"**  
→ `chmod +x start.sh`

---

## 📚 Docs

- **Setup:** `docs/TEAM_SETUP_ALL_PLATFORMS.md`
- **Git:** `docs/branching_strategy.md`
- **Quick Start:** `docs/quick_start_team.md`
- **IDE:** `docs/IDE_SETUP.md`

---

## 🎯 Your Assignment

Check `docs/quick_start_team.md` for your feature branch!
