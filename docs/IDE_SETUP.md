# IDE Setup Guide (PyCharm / VS Code)

## Problem: "ModuleNotFoundError: No module named 'flask'"

This happens when your IDE uses **system Python** instead of the **virtual environment**.

---

## ✅ Solution: Configure IDE to Use Virtual Environment

### **PyCharm**

#### Method 1: Set Python Interpreter (Recommended)
1. **Open Settings:**
   - `File` → `Settings` (Linux/Windows)
   - `PyCharm` → `Preferences` (macOS)

2. **Navigate to:**
   - `Project: hackathon-sofrecom-diag-raida` → `Python Interpreter`

3. **Add Interpreter:**
   - Click the gear icon ⚙️ → `Add`
   - Select `Existing environment`
   - Browse to: `/home/malik/PycharmProjects/hackathon-sofrecom-diag-raida/backend/venv/bin/python3`
   - Click `OK`

4. **Verify:**
   - You should see Flask, pandas, numpy, etc. in the package list
   - If not, the wrong interpreter is selected

#### Method 2: Run Configuration
1. **Edit Run Configuration:**
   - Click dropdown next to Run button → `Edit Configurations`

2. **Add New Configuration:**
   - Click `+` → `Python`
   - Name: `Diag-Raida API`
   - Script path: `/home/malik/PycharmProjects/hackathon-sofrecom-diag-raida/backend/run.py`
   - Python interpreter: Select the venv interpreter
   - Working directory: `/home/malik/PycharmProjects/hackathon-sofrecom-diag-raida/backend`
   - Click `OK`

3. **Run:**
   - Select "Diag-Raida API" from dropdown
   - Click Run ▶️

---

### **VS Code**

#### Method 1: Select Interpreter
1. **Open Command Palette:**
   - Press `Ctrl+Shift+P` (Linux/Windows)
   - Press `Cmd+Shift+P` (macOS)

2. **Type and Select:**
   - `Python: Select Interpreter`

3. **Choose:**
   - `./backend/venv/bin/python3`
   - Or browse to the venv path

4. **Verify:**
   - Bottom left should show: `Python 3.12.x ('venv')`

#### Method 2: Create launch.json
1. **Create `.vscode/launch.json`:**
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Diag-Raida API",
         "type": "python",
         "request": "launch",
         "program": "${workspaceFolder}/backend/run.py",
         "console": "integratedTerminal",
         "cwd": "${workspaceFolder}/backend",
         "env": {
           "FLASK_ENV": "development"
         },
         "python": "${workspaceFolder}/backend/venv/bin/python3"
       }
     ]
   }
   ```

2. **Run:**
   - Press `F5` or click Run → Start Debugging

---

## 🚀 Quick Fix (Terminal Method)

**Always works, regardless of IDE:**

```bash
cd /home/malik/PycharmProjects/hackathon-sofrecom-diag-raida/backend

# Activate venv
source venv/bin/activate

# You should see (venv) in your prompt
# (venv) malik@computer:~/...$ 

# Now run
python3 run.py
```

**Or one-liner:**
```bash
cd backend && source venv/bin/activate && python3 run.py
```

---

## 🔍 Verify Virtual Environment is Active

### Check 1: Prompt
```bash
# Should show (venv) before your prompt
(venv) malik@computer:~/backend$ 
```

### Check 2: Which Python
```bash
which python3
# Should output: /home/malik/.../backend/venv/bin/python3
# NOT: /usr/bin/python3
```

### Check 3: Check Flask
```bash
python3 -c "import flask; print(flask.__version__)"
# Should output: 3.0.3
# NOT: ModuleNotFoundError
```

---

## 📝 PyCharm Specific: Mark Directory as Sources Root

1. **Right-click on `backend` folder**
2. **Select:** `Mark Directory as` → `Sources Root`
3. **This helps with imports**

---

## ⚠️ Common Mistakes

### ❌ Running with System Python
```bash
# WRONG - uses system Python
/usr/bin/python3 run.py
python3 run.py  # (if venv not activated)
```

### ✅ Running with Virtual Environment
```bash
# CORRECT - uses venv Python
source venv/bin/activate
python3 run.py

# OR directly
./venv/bin/python3 run.py
```

---

## 🛠️ Troubleshooting

### Issue: "venv/bin/python3 not found"
**Solution:** Create virtual environment first
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: IDE still uses wrong Python
**Solution:** Restart IDE after changing interpreter

### Issue: "Import app could not be resolved"
**Solution:** 
- PyCharm: Mark `backend` as Sources Root
- VS Code: Set `"python.analysis.extraPaths": ["./backend"]` in settings.json

---

## ✅ Final Verification

After configuring IDE, run this test:

```bash
# In IDE terminal
cd backend
source venv/bin/activate
python3 -c "from app.main import create_app; app = create_app(); print('✅ App imports successfully!')"
```

Should output: `✅ App imports successfully!`

---

## 🎯 Best Practice

**Always activate venv before running:**
```bash
# Add to your shell startup (~/.bashrc or ~/.zshrc)
alias diagraida='cd /home/malik/PycharmProjects/hackathon-sofrecom-diag-raida/backend && source venv/bin/activate'

# Then just type:
diagraida
python3 run.py
```

---

## 📌 Summary

**The issue:** IDE uses system Python (`/usr/bin/python3.12`)  
**The fix:** Configure IDE to use venv Python (`backend/venv/bin/python3`)  
**Quick workaround:** Always run from terminal with activated venv

**Remember:** Virtual environments are isolated. System Python ≠ venv Python!
