# 🚀 START BUILDING - Feature Development Guide

## ✅ Main Branch is LOCKED

The baseline is complete and stable. **All development now happens in feature branches.**

---

## 🎯 Step 1: Create All Feature Branches

### Option A: Automatic (Recommended)

**Linux/Mac:**
```bash
./create_branches.sh
```

**Windows:**
```cmd
create_branches.bat
```

### Option B: Manual

```bash
git checkout main
git pull origin main

# Create each branch
git checkout -b feature/llm-integration
git push -u origin feature/llm-integration

git checkout main
git checkout -b feature/data-structures
git push -u origin feature/data-structures

# ... repeat for all branches
```

---

## 🌿 Feature Branches

### 1. **feature/llm-integration**
**Goal:** Integrate OpenRouter free LLM models  
**Key files:** `llm_service.py`, `prompts.py`  
**Priority:** HIGH

### 2. **feature/data-structures**
**Goal:** Create data models and sample diagnostic data  
**Key files:** `schemas.py`, `data_loader.py`, JSON data files  
**Priority:** HIGH

### 3. **feature/analysis-service**
**Goal:** Build core analysis with ML diagnostics  
**Key files:** `analysis_service.py`, `metrics.py`  
**Priority:** HIGH

### 4. **feature/evaluation-service**
**Goal:** Build evaluation and scoring logic  
**Key files:** `evaluation_service.py`, `scoring.py`  
**Priority:** MEDIUM

### 5. **feature/recommendation-service**
**Goal:** Build recommendation engine with LLM  
**Key files:** `recommendation_service.py`  
**Priority:** MEDIUM

### 6. **feature/ml-models**
**Goal:** Add ML models for prediction (optional)  
**Key files:** `ml_models.py`, `ml_service.py`  
**Priority:** LOW

---

## 👥 Step 2: Assign Team Members

Edit `FEATURE_BRANCHES.md` and assign:

```markdown
### 1. feature/llm-integration
**Owner:** [Your Name]

### 2. feature/data-structures
**Owner:** [Team Member 1]

### 3. feature/analysis-service
**Owner:** [Team Member 2]

### 4. feature/evaluation-service
**Owner:** [Team Member 3]

### 5. feature/recommendation-service
**Owner:** [Team Member 4]
```

---

## 🚀 Step 3: Start Working on Your Feature

### For You (LLM Integration):

```bash
# Checkout your branch
git checkout feature/llm-integration

# Install new dependencies
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install requests python-dotenv

# Start coding!
# See detailed tasks in FEATURE_BRANCHES.md
```

### For Team Members:

```bash
# Each member checks out their branch
git checkout feature/their-assigned-branch

# Start coding according to FEATURE_BRANCHES.md
```

---

## 📋 Development Workflow

### Daily Routine:

```bash
# 1. Start of day - update your branch
git checkout feature/your-branch
git pull origin feature/your-branch

# 2. Work on your feature
# - Write code
# - Write tests
# - Run tests locally

# 3. Test locally
cd backend
pytest tests/
./run_checks.sh  # or .bat on Windows

# 4. Commit and push
git add .
git commit -m "feat: what you did"
git push

# 5. CI/CD runs automatically
# - Check GitHub for results
# - Fix any failures
```

### Weekly Routine:

```bash
# Sync with main (weekly or when main updates)
git checkout main
git pull origin main
git checkout feature/your-branch
git merge main

# Resolve conflicts if any
# Test again
pytest tests/
git push
```

---

## 🎯 Example: Building LLM Integration

### Step 1: Update Config
```python
# backend/app/config.py
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
LLM_MODEL = 'meta-llama/llama-3.2-3b-instruct:free'
```

### Step 2: Create LLM Service
```python
# backend/app/services/llm_service.py
import requests
from flask import current_app

def call_llm(prompt, max_tokens=500):
    """Call OpenRouter LLM API"""
    # Implementation here
    pass
```

### Step 3: Create Prompts
```python
# backend/app/utils/prompts.py
def create_recommendation_prompt(student_data):
    """Generate prompt for recommendations"""
    # Implementation here
    pass
```

### Step 4: Write Tests
```python
# backend/tests/test_llm_service.py
def test_llm_call():
    """Test LLM service"""
    # Implementation here
    pass
```

### Step 5: Update Requirements
```txt
# backend/requirements.txt
requests==2.31.0
python-dotenv==1.0.1
```

---

## ✅ Definition of Done

Before creating a PR, ensure:

- [ ] Feature is complete and working
- [ ] All tests pass locally (`pytest tests/`)
- [ ] Code quality checks pass (`./run_checks.sh`)
- [ ] New tests added for new code
- [ ] Documentation updated
- [ ] No merge conflicts with main
- [ ] CI/CD passes on GitHub

---

## 🔄 Creating a Pull Request

### When Your Feature is Ready:

1. **Push final changes:**
   ```bash
   git push
   ```

2. **Go to GitHub**

3. **Create Pull Request:**
   - From: `feature/your-branch`
   - To: `main`

4. **Fill out PR template:**
   - Description
   - What changed
   - Tests added
   - Checklist

5. **Wait for CI/CD:** ✅ All checks must pass

6. **Get code review:** At least 1 approval

7. **Merge!** 🎉

---

## 🎓 Best Practices

### Commit Messages:
```bash
feat: add LLM integration with OpenRouter
fix: resolve API timeout issue
docs: update LLM configuration guide
test: add tests for recommendation service
refactor: simplify data validation logic
```

### Code Style:
```bash
# Before committing, run:
black app tests
isort app tests
flake8 app tests
pytest tests/
```

### Testing:
```python
# Always write tests for new features
def test_new_feature():
    result = my_function()
    assert result == expected
```

---

## 🆘 Getting Help

### Issues?

1. **Check documentation:**
   - `FEATURE_BRANCHES.md` - Detailed tasks
   - `docs/quick_start_team.md` - Setup help
   - `docs/CICD_GUIDE.md` - CI/CD help

2. **Ask in team chat:**
   - Share error message
   - Share what you tried
   - Share your branch name

3. **Create GitHub issue:**
   - Use issue templates
   - Tag relevant team members

---

## 📊 Progress Tracking

### Check Your Progress:

```bash
# See all branches
git branch -a

# See your commits
git log --oneline

# See what changed
git diff main
```

### Check Team Progress:

- Go to GitHub
- Check Pull Requests
- Check Actions (CI/CD status)
- Check Issues

---

## 🎉 Summary

**Main is locked** ✅  
**6 feature branches ready** ✅  
**Team can work in parallel** ✅  
**CI/CD catches issues** ✅  
**Clear workflow defined** ✅

---

## 🚀 Let's Build!

### You (Team Lead):
```bash
git checkout feature/llm-integration
# Start building LLM integration
```

### Team Members:
```bash
# Each picks their branch
git checkout feature/their-branch
# Start building their feature
```

---

**📚 Full details in `FEATURE_BRANCHES.md`**

**🎯 Pick your branch and start coding!**
