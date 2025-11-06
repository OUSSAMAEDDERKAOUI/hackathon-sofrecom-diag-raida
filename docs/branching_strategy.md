# Git Branching Strategy - Diag-Raida Team

## Overview
This document defines the branching strategy for our 5-person team to avoid conflicts and maintain code quality.

---

## Branch Structure

### **Main Branches**

#### 1. `main` (Protected)
- **Purpose:** Production-ready code only
- **Rules:**
  - ✅ Always stable and runnable
  - ✅ Requires pull request + code review
  - ❌ No direct commits
  - ❌ No force pushes

#### 2. `develop` (Integration Branch)
- **Purpose:** Integration branch for features
- **Rules:**
  - ✅ All features merge here first
  - ✅ Tested before merging to `main`
  - ❌ No direct commits (use feature branches)

---

## Feature Branches

### **Naming Convention**
```
feature/<feature-name>
fix/<bug-name>
hotfix/<critical-fix>
```

### **Examples:**
- `feature/ml-models`
- `feature/llm-integration`
- `feature/data-loaders`
- `feature/evaluation-service`
- `feature/recommendation-service`
- `fix/analysis-validation`
- `hotfix/critical-api-error`

---

## Workflow

### **1. Starting New Work**
```bash
# Always start from latest develop
git checkout develop
git pull origin develop

# Create your feature branch
git checkout -b feature/your-feature-name
```

### **2. Working on Your Feature**
```bash
# Make changes and commit regularly
git add .
git commit -m "feat: descriptive message"

# Push to remote
git push origin feature/your-feature-name
```

### **3. Keeping Your Branch Updated**
```bash
# Regularly sync with develop to avoid conflicts
git checkout develop
git pull origin develop
git checkout feature/your-feature-name
git merge develop

# Or use rebase (cleaner history)
git rebase develop
```

### **4. Creating Pull Request**
1. Push your feature branch to GitHub
2. Open PR: `feature/your-feature-name` → `develop`
3. Add description of changes
4. Request review from at least 1 team member
5. Address review comments
6. Merge after approval

### **5. Merging to Main**
- Only merge `develop` → `main` when:
  - All features are tested
  - Team agrees it's ready
  - CI/CD passes (if configured)

---

## Feature Branch Assignments

### **Suggested Division for 5 Team Members:**

#### **Member 1: Data & ML Models**
- Branch: `feature/ml-models`
- Tasks:
  - Decision tree model implementation
  - Model training and persistence (joblib)
  - Model evaluation metrics

#### **Member 2: Data Loaders & Utilities**
- Branch: `feature/data-infrastructure`
- Tasks:
  - `data_loader.py` implementation
  - JSON schema for questions/resources
  - Helper utilities
  - Input validation

#### **Member 3: Analysis & Evaluation Services**
- Branch: `feature/analysis-evaluation`
- Tasks:
  - `analysis_service.py` full implementation
  - `evaluation_service.py` full implementation
  - Integration with ML models

#### **Member 4: LLM Integration & Recommendations**
- Branch: `feature/llm-recommendations`
- Tasks:
  - LLM API integration (OpenAI/Anthropic)
  - `recommendation_service.py` implementation
  - Prompt engineering

#### **Member 5: Testing & Documentation**
- Branch: `feature/testing-docs`
- Tasks:
  - Unit tests for all services
  - Integration tests for routes
  - API documentation
  - Deployment scripts

---

## Commit Message Convention

Use semantic commit messages:

```
feat: add new feature
fix: bug fix
docs: documentation changes
test: add tests
refactor: code refactoring
style: formatting changes
chore: maintenance tasks
```

**Examples:**
```bash
git commit -m "feat: implement decision tree model training"
git commit -m "fix: handle empty data in analysis service"
git commit -m "test: add unit tests for evaluation service"
git commit -m "docs: update API endpoint documentation"
```

---

## Conflict Resolution

### **If You Get Conflicts:**

1. **Don't Panic!** Conflicts are normal
2. **Communicate** with your team
3. **Resolve locally:**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout feature/your-feature
   git merge develop
   # Fix conflicts in your editor
   git add .
   git commit -m "merge: resolve conflicts with develop"
   git push origin feature/your-feature
   ```

---

## Best Practices

### ✅ **DO:**
- Pull from `develop` before starting work
- Commit small, logical changes
- Write descriptive commit messages
- Test your code before pushing
- Keep branches short-lived (1-3 days max)
- Delete branches after merging
- Communicate with team about overlapping work

### ❌ **DON'T:**
- Commit directly to `main` or `develop`
- Push broken code
- Leave branches unmerged for weeks
- Force push to shared branches
- Commit sensitive data (API keys, passwords)

---

## Quick Reference Commands

```bash
# Check current branch
git branch

# See all branches
git branch -a

# Switch branches
git checkout branch-name

# Create and switch to new branch
git checkout -b feature/new-feature

# Update your branch with latest develop
git checkout develop && git pull
git checkout feature/your-feature && git merge develop

# Delete local branch (after merging)
git branch -d feature/old-feature

# Delete remote branch
git push origin --delete feature/old-feature

# See what changed
git status
git diff

# Undo last commit (keep changes)
git reset --soft HEAD~1
```

---

## Emergency Procedures

### **Hotfix for Production Bug:**
```bash
# Create hotfix from main
git checkout main
git pull origin main
git checkout -b hotfix/critical-bug

# Fix the bug
# ... make changes ...

# Commit and push
git commit -m "hotfix: fix critical bug in API"
git push origin hotfix/critical-bug

# Create PR to main AND develop
# Merge immediately after review
```

---

## Questions?
- Ask in team chat before making risky changes
- When in doubt, create a branch!
- Better to over-communicate than under-communicate

---

**Remember:** The goal is to work in parallel without stepping on each other's toes. Use branches liberally!
