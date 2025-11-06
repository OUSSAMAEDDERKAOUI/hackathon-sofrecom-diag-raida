# 🚀 Team Setup Guide - All Platforms

**For:** Windows, Ubuntu, Debian, macOS  
**Time:** 5-10 minutes  
**Goal:** Get the Flask API running on your machine

---

## 📋 Prerequisites Check

### All Platforms Need:
- **Python 3.12** (or 3.10+)
- **Git**
- **Terminal/Command Prompt**
- **Internet connection** (for pip install)

### Check Python Version:
```bash
python3 --version
# OR on Windows:
python --version

# Should show: Python 3.12.x or 3.10+
```

---

## 🪟 WINDOWS SETUP

### Step 1: Clone Repository
```cmd
cd C:\Users\YourName\Documents
git clone <repository-url>
cd hackathon-sofrecom-diag-raida\backend
```

### Step 2: Create Virtual Environment
```cmd
python -m venv venv
```

### Step 3: Activate Virtual Environment
```cmd
venv\Scripts\activate

REM You should see (venv) in your prompt:
REM (venv) C:\Users\...\backend>
```

### Step 4: Install Dependencies
```cmd
pip install -r requirements.txt
```

### Step 5: Run the App
```cmd
python run.py
```

### Step 6: Test It Works
Open another Command Prompt and run:
```cmd
curl http://localhost:5000/health

REM If curl not available, open browser:
REM http://localhost:5000/health
```

### Step 7: Run Tests
```cmd
pytest tests\
```

---

## 🐧 UBUNTU / DEBIAN SETUP

### Step 1: Clone Repository
```bash
cd ~
git clone <repository-url>
cd hackathon-sofrecom-diag-raida/backend
```

### Step 2: Install Python 3.12 (if needed)
```bash
# Check version first
python3 --version

# If not 3.12, install it:
# Ubuntu:
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip

# Debian:
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

### Step 3: Create Virtual Environment
```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment
```bash
source venv/bin/activate

# You should see (venv) in your prompt:
# (venv) user@computer:~/backend$
```

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 6: Run the App
```bash
# Option A: Using helper script
./start.sh

# Option B: Manual
python3 run.py
```

### Step 7: Test It Works
Open another terminal:
```bash
curl http://localhost:5000/health
```

### Step 8: Run Tests
```bash
pytest tests/
```

---

## 🍎 macOS SETUP

### Step 1: Clone Repository
```bash
cd ~
git clone <repository-url>
cd hackathon-sofrecom-diag-raida/backend
```

### Step 2: Install Python 3.12 (if needed)
```bash
# Check version first
python3 --version

# If not installed, use Homebrew:
brew install python@3.12
```

### Step 3: Create Virtual Environment
```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment
```bash
source venv/bin/activate

# You should see (venv) in your prompt
```

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 6: Run the App
```bash
./start.sh
# OR
python3 run.py
```

### Step 7: Test It Works
```bash
curl http://localhost:5000/health
```

### Step 8: Run Tests
```bash
pytest tests/
```

---

## ✅ Verification Checklist

After setup, verify everything works:

### 1. Virtual Environment is Active
**Windows:**
```cmd
where python
REM Should show: C:\...\backend\venv\Scripts\python.exe
```

**Linux/Mac:**
```bash
which python3
# Should show: /home/.../backend/venv/bin/python3
```

### 2. Flask is Installed
```bash
# All platforms (with venv active):
python -c "import flask; print(flask.__version__)"
# Should output: 3.0.3
```

### 3. App Starts Successfully
```bash
# You should see:
 * Serving Flask app 'app.main'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 4. Health Check Works
**Browser:** Open `http://localhost:5000/health`

**Command Line:**
```bash
curl http://localhost:5000/health
```

**Expected Response:**
```json
{
  "service": "Diag-Raida API",
  "status": "healthy",
  "version": "v1"
}
```

### 5. All Tests Pass
```bash
pytest tests/
# Should show: 6 passed
```

---

## 🐛 Common Issues & Solutions

### Issue 1: "python3: command not found" (Windows)
**Solution:** Use `python` instead of `python3` on Windows
```cmd
python --version
python -m venv venv
python run.py
```

### Issue 2: "ModuleNotFoundError: No module named 'flask'"
**Cause:** Virtual environment not activated

**Windows Solution:**
```cmd
cd backend
venv\Scripts\activate
python run.py
```

**Linux/Mac Solution:**
```bash
cd backend
source venv/bin/activate
python3 run.py
```

### Issue 3: "Permission denied: ./start.sh" (Linux/Mac)
**Solution:**
```bash
chmod +x start.sh
./start.sh
```

### Issue 4: "Address already in use"
**Solution:**

**Windows:**
```cmd
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Linux/Mac:**
```bash
lsof -ti:5000 | xargs kill -9
```

### Issue 5: "pip: command not found"
**Solution:**

**Windows:**
```cmd
python -m pip install -r requirements.txt
```

**Linux/Mac:**
```bash
python3 -m pip install -r requirements.txt
```

### Issue 6: curl not available (Windows)
**Solutions:**
1. Use browser: `http://localhost:5000/health`
2. Install curl: `winget install curl`
3. Use PowerShell:
```powershell
Invoke-WebRequest -Uri http://localhost:5000/health
```

---

## 🔧 IDE Setup (All Platforms)

### Visual Studio Code

1. **Install Python Extension**
   - Open VS Code
   - Extensions → Search "Python" → Install

2. **Select Interpreter**
   - `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
   - Type: "Python: Select Interpreter"
   - Choose: `./backend/venv/bin/python` (or `venv\Scripts\python.exe` on Windows)

3. **Run Configuration**
   - Create `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Flask API",
         "type": "python",
         "request": "launch",
         "program": "${workspaceFolder}/backend/run.py",
         "console": "integratedTerminal",
         "cwd": "${workspaceFolder}/backend"
       }
     ]
   }
   ```

### PyCharm

1. **Open Project**
   - File → Open → Select `hackathon-sofrecom-diag-raida`

2. **Configure Interpreter**
   - File → Settings → Project → Python Interpreter
   - Click ⚙️ → Add → Existing environment
   - Browse to: `backend/venv/bin/python3` (or `backend\venv\Scripts\python.exe` on Windows)

3. **Run Configuration**
   - Run → Edit Configurations → + → Python
   - Script path: `backend/run.py`
   - Working directory: `backend/`
   - Python interpreter: Select venv

---

## 📝 Quick Reference Card

### Windows Commands
```cmd
REM Activate venv
venv\Scripts\activate

REM Run app
python run.py

REM Run tests
pytest tests\

REM Deactivate venv
deactivate
```

### Linux/Mac Commands
```bash
# Activate venv
source venv/bin/activate

# Run app
python3 run.py
# OR
./start.sh

# Run tests
pytest tests/

# Deactivate venv
deactivate
```

---

## 🎯 First Day Checklist

- [ ] Clone repository
- [ ] Create virtual environment
- [ ] Activate virtual environment (see `(venv)` in prompt)
- [ ] Install dependencies
- [ ] Run app successfully
- [ ] Test health endpoint
- [ ] Run all tests (6 passing)
- [ ] Read `docs/quick_start_team.md`
- [ ] Read `docs/branching_strategy.md`
- [ ] Create your feature branch
- [ ] Make a test commit

---

## 🆘 Still Having Issues?

### Check These:
1. **Python version:** `python --version` or `python3 --version` (need 3.10+)
2. **Venv active:** Look for `(venv)` in your prompt
3. **Right directory:** Should be in `backend/` folder
4. **Dependencies installed:** Run `pip list | grep Flask` (should show Flask 3.0.3)

### Get Help:
1. Check `docs/IDE_SETUP.md` for IDE-specific issues
2. Check `docs/quick_start_team.md` for detailed troubleshooting
3. Ask in team chat with:
   - Your OS (Windows/Ubuntu/Debian/Mac)
   - Error message (full text)
   - What command you ran

---

## 🎉 Success!

If you see this, you're ready:
```
✅ Virtual environment activated
✅ Flask app running on http://localhost:5000
✅ Health check returns: {"status": "healthy"}
✅ All 6 tests passing
```

**Next:** Read your feature assignment in `docs/quick_start_team.md`

---

## 📚 Additional Resources

- **Quick Start:** `docs/quick_start_team.md`
- **Branching Strategy:** `docs/branching_strategy.md`
- **IDE Setup:** `docs/IDE_SETUP.md`
- **Backend Guide:** `backend/README.md`

---

**Remember:** Always activate your virtual environment before working!
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`
