# 🧪 How Your Team Will Test Everything

## 📋 Overview

Your team uses different operating systems:
- **You:** Ubuntu
- **Team Member(s):** Windows
- **Team Member:** Debian

**Good news:** Everything works cross-platform! ✅

---

## 🎯 What Each Team Member Should Do

### Step 1: Pull from Main
```bash
git clone <repository-url>
cd hackathon-sofrecom-diag-raida
```

### Step 2: Follow Platform-Specific Setup

**📖 Full Guide:** `docs/TEAM_SETUP_ALL_PLATFORMS.md`

#### Windows Users:
```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python test_setup.py
```

#### Ubuntu/Debian Users:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 test_setup.py
```

### Step 3: Verify Setup
The `test_setup.py` script will check:
- ✅ Python version (3.10+)
- ✅ Virtual environment active
- ✅ All packages installed (Flask, pandas, etc.)
- ✅ App imports successfully
- ✅ All routes registered
- ✅ Configuration loaded

**Expected output:**
```
🎉 SUCCESS! Your setup is complete and working!
```

### Step 4: Run the App

**Windows:**
```cmd
start.bat
```

**Ubuntu/Debian:**
```bash
./start.sh
```

### Step 5: Test API Endpoints

**Option A: Using curl**
```bash
curl http://localhost:5000/health
curl http://localhost:5000/
curl -X POST http://localhost:5000/api/analysis/ -H "Content-Type: application/json" -d "{\"test\":\"data\"}"
```

**Option B: Using browser**
- Open: `http://localhost:5000/health`
- Open: `http://localhost:5000/`

**Option C: Using PowerShell (Windows)**
```powershell
Invoke-WebRequest -Uri http://localhost:5000/health
```

### Step 6: Run Tests
```bash
# All platforms (with venv active)
pytest tests/

# Should show: 6 passed
```

---

## ✅ Success Criteria

Each team member should verify:

### 1. Setup Script Passes
```bash
python test_setup.py
# All checks should be ✅ PASS
```

### 2. App Starts
```
✅ Virtual environment activated
🚀 Starting Diag-Raida API...
 * Running on http://127.0.0.1:5000
```

### 3. Health Check Works
```json
{
  "service": "Diag-Raida API",
  "status": "healthy",
  "version": "v1"
}
```

### 4. All Tests Pass
```
====== 6 passed in 0.11s ======
```

### 5. Can Create Feature Branch
```bash
git checkout develop
git pull origin develop
git checkout -b feature/test-branch
# Should work without errors
```

---

## 🐛 Platform-Specific Issues

### Windows-Specific

#### Issue: "python3: command not found"
**Solution:** Use `python` instead of `python3`
```cmd
python --version
python run.py
```

#### Issue: curl not available
**Solutions:**
1. Use browser: `http://localhost:5000/health`
2. Use PowerShell: `Invoke-WebRequest -Uri http://localhost:5000/health`
3. Install curl: `winget install curl`

#### Issue: Script execution disabled
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Ubuntu/Debian-Specific

#### Issue: Python 3.12 not available
**Ubuntu:**
```bash
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip
```

**Debian:**
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

#### Issue: "Permission denied: ./start.sh"
**Solution:**
```bash
chmod +x start.sh
./start.sh
```

---

## 📊 Testing Checklist for Each Platform

### Windows Testing
- [ ] Clone repository
- [ ] Create venv with `python -m venv venv`
- [ ] Activate with `venv\Scripts\activate`
- [ ] Install dependencies
- [ ] Run `python test_setup.py` (all pass)
- [ ] Run `start.bat` (app starts)
- [ ] Test health endpoint (browser or PowerShell)
- [ ] Run `pytest tests\` (6 passed)
- [ ] Create feature branch

### Ubuntu Testing
- [ ] Clone repository
- [ ] Create venv with `python3 -m venv venv`
- [ ] Activate with `source venv/bin/activate`
- [ ] Install dependencies
- [ ] Run `python3 test_setup.py` (all pass)
- [ ] Run `./start.sh` (app starts)
- [ ] Test with `curl http://localhost:5000/health`
- [ ] Run `pytest tests/` (6 passed)
- [ ] Create feature branch

### Debian Testing
- [ ] Clone repository
- [ ] Create venv with `python3 -m venv venv`
- [ ] Activate with `source venv/bin/activate`
- [ ] Install dependencies
- [ ] Run `python3 test_setup.py` (all pass)
- [ ] Run `./start.sh` (app starts)
- [ ] Test with `curl http://localhost:5000/health`
- [ ] Run `pytest tests/` (6 passed)
- [ ] Create feature branch

---

## 🎓 What to Tell Your Team

### In Team Chat:
```
🚀 Main branch is ready! Please test on your machine:

1️⃣ Clone repo
2️⃣ Follow setup in: docs/TEAM_SETUP_ALL_PLATFORMS.md
3️⃣ Run: python test_setup.py (or python3 on Linux)
4️⃣ Start app: start.bat (Windows) or ./start.sh (Linux)
5️⃣ Test: curl http://localhost:5000/health
6️⃣ Run tests: pytest tests/

📚 Quick reference: docs/QUICK_REFERENCE.md

⚠️ Windows users: Use "python" not "python3"
⚠️ Linux users: Use "python3" and activate venv first

Report any issues with:
- Your OS (Windows/Ubuntu/Debian)
- Error message
- What command you ran
```

---

## 🔍 How to Verify Cross-Platform Compatibility

### You (Ubuntu) - Already Tested ✅
- App runs: ✅
- Tests pass: ✅
- Setup script works: ✅

### Windows Team Member Should See:
```cmd
C:\...\backend> python test_setup.py
============================================================
🔍 Diag-Raida Setup Verification
============================================================
✓ Python version: 3.12.x
  ✅ Python version is compatible
...
🎉 SUCCESS! Your setup is complete and working!
```

### Debian Team Member Should See:
```bash
user@debian:~/backend$ python3 test_setup.py
============================================================
🔍 Diag-Raida Setup Verification
============================================================
✓ Python version: 3.12.x
  ✅ Python version is compatible
...
🎉 SUCCESS! Your setup is complete and working!
```

---

## 📁 Files Created for Cross-Platform Support

### For Windows:
- `backend/start.bat` - Windows startup script
- Uses `python` instead of `python3`
- Uses `\` instead of `/` for paths

### For Linux/Mac:
- `backend/start.sh` - Bash startup script
- Uses `python3`
- Uses `/` for paths

### For All Platforms:
- `backend/test_setup.py` - Universal setup verification
- `docs/TEAM_SETUP_ALL_PLATFORMS.md` - Complete guide
- `docs/QUICK_REFERENCE.md` - One-page cheat sheet

---

## 🎯 Expected Timeline

### Day 1 (Today):
- You push to main ✅
- You test on Ubuntu ✅

### Day 2 (Tomorrow):
- Team members pull from main
- Each tests on their OS
- Report any issues
- Fix platform-specific issues if any

### Day 3:
- Everyone confirmed working
- Create feature branches
- Start development

---

## 🆘 If Something Doesn't Work

### Debugging Steps:
1. **Check Python version:** `python --version` (need 3.10+)
2. **Check venv active:** Look for `(venv)` in prompt
3. **Run setup test:** `python test_setup.py`
4. **Check error message:** Copy full error text
5. **Check documentation:** `docs/TEAM_SETUP_ALL_PLATFORMS.md`

### Report Issues With:
- Operating system (Windows 10/11, Ubuntu 22.04, Debian 12, etc.)
- Python version
- Full error message
- Command that caused error
- Screenshot if helpful

---

## ✅ Final Verification

Before declaring "ready for team":

- [x] Ubuntu (you) - Tested ✅
- [ ] Windows - Team member tests
- [ ] Debian - Team member tests
- [ ] All documentation complete ✅
- [ ] Cross-platform scripts created ✅
- [ ] Setup verification script works ✅

---

## 🎉 Success Looks Like

**All 5 team members can:**
1. Clone the repo
2. Run setup in 5-10 minutes
3. See `test_setup.py` pass all checks
4. Start the app
5. Test the API
6. Run all tests (6 passing)
7. Create their feature branch
8. Start coding

**No platform-specific issues blocking anyone!**

---

**Next:** Push to main and ask team to test on their machines! 🚀
