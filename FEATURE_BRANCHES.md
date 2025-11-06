# 🌿 Feature Branches - Development Plan

## 📋 Overview

Main branch is now **LOCKED** as the stable baseline. All development happens in feature branches.

---

## 🎯 Feature Branches to Create

### 1. **feature/llm-integration**
**Owner:** [Assign team member]  
**Purpose:** Integrate OpenRouter LLM for intelligent recommendations

**Tasks:**
- [ ] Add OpenRouter API client
- [ ] Configure free LLM models (Llama 3.2, Gemma 2, Mistral)
- [ ] Create LLM service wrapper
- [ ] Add prompt templates for math recommendations
- [ ] Handle API errors and fallbacks
- [ ] Add LLM response caching
- [ ] Write tests for LLM service

**Files to create/modify:**
- `backend/app/services/llm_service.py`
- `backend/app/utils/prompts.py`
- `backend/app/config.py` (add LLM config)
- `backend/requirements.txt` (add requests, python-dotenv)
- `backend/tests/test_llm_service.py`

---

### 2. **feature/data-structures**
**Owner:** [Assign team member]  
**Purpose:** Create data models and sample diagnostic data

**Tasks:**
- [ ] Define student response data structure
- [ ] Create diagnostic question schemas
- [ ] Build sample math diagnostic data (JSON)
- [ ] Create data validation utilities
- [ ] Build data loader service
- [ ] Add data transformation utilities
- [ ] Write tests for data structures

**Files to create/modify:**
- `backend/app/models/schemas.py`
- `backend/app/utils/validators.py`
- `backend/app/services/data_loader.py`
- `backend/data/diagnostic_questions.json`
- `backend/data/sample_responses.json`
- `backend/tests/test_data_structures.py`

---

### 3. **feature/analysis-service**
**Owner:** [Assign team member]  
**Purpose:** Build core analysis service with ML diagnostics

**Tasks:**
- [ ] Implement response analysis logic
- [ ] Calculate accuracy metrics
- [ ] Identify weak areas (algebra, geometry, etc.)
- [ ] Pattern recognition for common mistakes
- [ ] Time-based performance analysis
- [ ] Generate diagnostic insights
- [ ] Write comprehensive tests

**Files to create/modify:**
- `backend/app/services/analysis_service.py` (replace placeholder)
- `backend/app/utils/metrics.py`
- `backend/app/utils/patterns.py`
- `backend/tests/test_analysis_service.py`

---

### 4. **feature/evaluation-service**
**Owner:** [Assign team member]  
**Purpose:** Build evaluation and scoring logic

**Tasks:**
- [ ] Implement scoring algorithms
- [ ] Calculate difficulty-adjusted scores
- [ ] Generate performance reports
- [ ] Create skill level assessment
- [ ] Build progress tracking
- [ ] Add comparative analysis
- [ ] Write comprehensive tests

**Files to create/modify:**
- `backend/app/services/evaluation_service.py` (replace placeholder)
- `backend/app/utils/scoring.py`
- `backend/app/models/evaluation.py`
- `backend/tests/test_evaluation_service.py`

---

### 5. **feature/recommendation-service**
**Owner:** [Assign team member]  
**Purpose:** Build recommendation engine with LLM integration

**Tasks:**
- [ ] Integrate with LLM service
- [ ] Create recommendation logic
- [ ] Generate personalized study plans
- [ ] Suggest practice exercises
- [ ] Provide learning resources
- [ ] Add difficulty progression
- [ ] Write comprehensive tests

**Files to create/modify:**
- `backend/app/services/recommendation_service.py` (replace placeholder)
- `backend/app/utils/recommendations.py`
- `backend/tests/test_recommendation_service.py`

---

### 6. **feature/ml-models** (Optional/Advanced)
**Owner:** [Assign team member]  
**Purpose:** Add ML models for prediction and classification

**Tasks:**
- [ ] Train decision tree classifier
- [ ] Build difficulty prediction model
- [ ] Create student clustering model
- [ ] Add model persistence (joblib)
- [ ] Build model training pipeline
- [ ] Add model evaluation metrics
- [ ] Write tests for ML models

**Files to create/modify:**
- `backend/app/models/ml_models.py`
- `backend/app/services/ml_service.py`
- `backend/models/saved/` (trained models)
- `backend/scripts/train_models.py`
- `backend/tests/test_ml_models.py`

---

## 🚀 How to Create and Work on Feature Branches

### Step 1: Create Your Feature Branch
```bash
cd /home/malik/PycharmProjects/hackathon-sofrecom-diag-raida

# Make sure main is up to date
git checkout main
git pull origin main

# Create your feature branch
git checkout -b feature/your-feature-name

# Push to remote
git push -u origin feature/your-feature-name
```

### Step 2: Work on Your Feature
```bash
# Make changes
# Test locally
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
pytest tests/
./run_checks.sh  # Windows: run_checks.bat

# Commit frequently
git add .
git commit -m "feat: describe what you did"
git push
```

### Step 3: Keep Your Branch Updated
```bash
# Regularly sync with main
git checkout main
git pull origin main
git checkout feature/your-feature-name
git merge main

# Resolve any conflicts
# Test again
pytest tests/
```

### Step 4: Create Pull Request
```bash
# When feature is complete:
# 1. Push final changes
git push

# 2. Go to GitHub
# 3. Create PR: feature/your-feature-name → main
# 4. Fill out PR template
# 5. Wait for CI/CD checks ✅
# 6. Get code review
# 7. Merge!
```

---

## 📋 Branch Naming Convention

**Format:** `feature/descriptive-name`

**Examples:**
- ✅ `feature/llm-integration`
- ✅ `feature/data-structures`
- ✅ `feature/analysis-service`
- ❌ `malik-feature` (not descriptive)
- ❌ `new-stuff` (too vague)

---

## 🔒 Main Branch Protection

**Rules:**
- ❌ No direct commits to main
- ✅ All changes via Pull Requests
- ✅ All CI/CD checks must pass
- ✅ At least 1 code review required
- ✅ No merge conflicts allowed

---

## 🎯 Development Workflow

```
main (stable baseline)
  ↓
feature/llm-integration ────────┐
feature/data-structures ────────┤
feature/analysis-service ───────┤→ Pull Requests → main
feature/evaluation-service ─────┤
feature/recommendation-service ─┘
```

---

## 📊 Progress Tracking

### Week 1: Foundation
- [ ] Create all feature branches
- [ ] Assign team members
- [ ] Set up development environments
- [ ] Start parallel development

### Week 2: Core Features
- [ ] Complete data structures
- [ ] Complete analysis service
- [ ] Complete evaluation service
- [ ] LLM integration working

### Week 3: Integration
- [ ] Complete recommendation service
- [ ] Integrate all services
- [ ] End-to-end testing
- [ ] Documentation updates

### Week 4: Polish & Deploy
- [ ] Bug fixes
- [ ] Performance optimization
- [ ] Final testing
- [ ] Deployment

---

## 🆘 Common Issues

### Merge Conflicts
```bash
# Update from main
git checkout main && git pull
git checkout feature/your-feature
git merge main

# Fix conflicts in files
# Then:
git add .
git commit -m "fix: resolve merge conflicts"
git push
```

### CI/CD Failures
```bash
# Run checks locally first
./run_checks.sh  # or .bat on Windows

# Fix issues
# Commit and push
git add .
git commit -m "fix: resolve CI/CD issues"
git push
```

### Lost Changes
```bash
# Check what changed
git status
git diff

# Recover deleted files
git restore <file>

# Undo last commit (keep changes)
git reset --soft HEAD~1
```

---

## 📚 Resources

- **Branching Strategy:** `docs/branching_strategy.md`
- **Quick Start:** `docs/quick_start_team.md`
- **CI/CD Guide:** `docs/CICD_GUIDE.md`
- **Backend README:** `backend/README.md`

---

## ✅ Quick Reference

```bash
# Create branch
git checkout -b feature/name

# Push branch
git push -u origin feature/name

# Update from main
git checkout main && git pull
git checkout feature/name && git merge main

# Run tests
cd backend && pytest tests/

# Run checks
./run_checks.sh  # or .bat

# Create PR
# Go to GitHub → Pull Requests → New PR
```

---

**🚀 Ready to build! Pick your feature branch and start coding!**
