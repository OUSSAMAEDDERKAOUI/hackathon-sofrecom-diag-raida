# 🚀 CI/CD Pipeline Guide

## Overview

Automated checks run on **every push and pull request** to catch issues before they reach main branches.

---

## 🔄 What Runs Automatically

### On Every Push to Any Branch

#### 1. **Multi-Platform Testing** (`ci.yml`)
- ✅ Tests on **Ubuntu** and **Windows**
- ✅ Tests on **Python 3.10, 3.11, 3.12**
- ✅ Runs all pytest tests
- ✅ Verifies setup with `test_setup.py`
- ✅ Checks Flask app imports correctly

**Matrix:** 2 OS × 3 Python versions = 6 test combinations

#### 2. **Code Quality Checks** (`ci.yml`)
- ✅ **Black** - Code formatting
- ✅ **isort** - Import sorting
- ✅ **flake8** - Linting (syntax errors, undefined names)

#### 3. **Security Scanning** (`ci.yml`)
- ✅ **Safety** - Checks for vulnerable dependencies
- ✅ **Bandit** - Scans code for security issues

### On Pull Requests Only

#### 4. **PR Validation** (`pr-checks.yml`)
- ✅ PR title format (must start with `feat:|fix:|docs:|test:|refactor:|style:|chore:|hotfix:`)
- ✅ Merge conflict detection
- ✅ Branch naming convention check
- ✅ Test coverage report generation

#### 5. **Changed Files Analysis** (`pr-checks.yml`)
- ✅ Warns if code changed but no tests added
- ✅ Detects potentially sensitive files
- ✅ Checks if documentation needs updating

### On Push to Main Branch

#### 6. **Deployment Validation** (`deploy.yml`)
- ✅ Runs all tests
- ✅ Verifies production config (debug mode OFF)
- ✅ Checks for TODO/FIXME in critical files
- ✅ Creates release tags automatically

---

## 📊 CI/CD Status Badges

Add these to your README.md:

```markdown
![CI/CD](https://github.com/YOUR_USERNAME/hackathon-sofrecom-diag-raida/workflows/CI/CD%20Pipeline/badge.svg)
![PR Checks](https://github.com/YOUR_USERNAME/hackathon-sofrecom-diag-raida/workflows/Pull%20Request%20Checks/badge.svg)
```

---

## 🏃 Running Checks Locally

### Before Committing (Recommended)

**Linux/Mac:**
```bash
cd backend
./run_checks.sh
```

**Windows:**
```cmd
cd backend
run_checks.bat
```

This runs:
1. Black formatting check
2. isort import sorting
3. flake8 linting
4. pytest tests
5. bandit security scan

### Individual Checks

```bash
# Format code
black app tests

# Sort imports
isort app tests

# Lint code
flake8 app tests

# Run tests
pytest tests/

# Security scan
bandit -r app

# Test coverage
pytest tests/ --cov=app --cov-report=html
```

---

## ✅ What Must Pass Before Merging

### Critical (Must Pass)
- ✅ All pytest tests (6/6)
- ✅ No Python syntax errors
- ✅ Flask app imports successfully
- ✅ Works on Ubuntu and Windows
- ✅ Works on Python 3.10, 3.11, 3.12

### Warnings (Should Fix)
- ⚠️ Code formatting issues
- ⚠️ Import sorting issues
- ⚠️ Linting warnings
- ⚠️ Security vulnerabilities
- ⚠️ Missing tests for new code

---

## 🔴 What Happens If Checks Fail

### On Push to Feature Branch
1. ❌ CI/CD runs and fails
2. 🔔 You get a notification
3. 📧 Email with failure details
4. ✏️ Fix the issues
5. 🔄 Push again (CI/CD runs automatically)

### On Pull Request
1. ❌ PR checks fail
2. 🚫 **Cannot merge** until fixed
3. 📝 PR shows red X with details
4. ✏️ Fix issues and push
5. ✅ PR checks run again automatically

### On Push to Main (Protected)
1. 🚫 Direct push blocked (if branch protection enabled)
2. ✅ Must go through PR process
3. ✅ All checks must pass before merge

---

## 📋 PR Title Format

Your PR title **must** start with one of these:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Adding tests
- `refactor:` - Code refactoring
- `style:` - Formatting changes
- `chore:` - Maintenance tasks
- `hotfix:` - Critical production fix

**Examples:**
- ✅ `feat: add ML model training pipeline`
- ✅ `fix: resolve analysis service validation error`
- ✅ `docs: update API endpoint documentation`
- ❌ `Added new feature` (missing prefix)
- ❌ `Update code` (not descriptive)

---

## 🌿 Branch Naming Convention

Branches **should** follow this pattern:

- `feature/*` - New features
- `fix/*` - Bug fixes
- `hotfix/*` - Critical fixes
- `docs/*` - Documentation
- `test/*` - Test additions

**Examples:**
- ✅ `feature/ml-models`
- ✅ `fix/analysis-validation`
- ✅ `docs/api-endpoints`
- ⚠️ `malik-feature` (not following convention)

---

## 🔧 Fixing Common CI/CD Failures

### "Tests failed"
```bash
# Run tests locally to see what failed
cd backend
pytest tests/ -v

# Fix the failing tests
# Push again
```

### "Code formatting issues"
```bash
# Auto-fix formatting
cd backend
black app tests
isort app tests

# Commit and push
git add .
git commit -m "style: fix code formatting"
git push
```

### "Linting errors"
```bash
# See what's wrong
cd backend
flake8 app tests

# Fix the issues manually
# Then push
```

### "Merge conflicts detected"
```bash
# Update from base branch
git checkout develop
git pull origin develop
git checkout your-feature-branch
git merge develop

# Resolve conflicts
# Then push
```

### "PR title format incorrect"
```bash
# On GitHub, edit your PR title
# Change from: "Added new feature"
# To: "feat: add new feature"
```

---

## 📈 Viewing CI/CD Results

### On GitHub

1. **Go to your PR or commit**
2. **Scroll down to checks section**
3. **Click "Details" on any check**
4. **View logs and errors**

### Check Status Indicators

- ✅ Green checkmark = Passed
- ❌ Red X = Failed
- 🟡 Yellow dot = Running
- ⚪ Gray circle = Pending

---

## 🎯 Best Practices

### Before Pushing

1. ✅ Run `./run_checks.sh` (or `.bat` on Windows)
2. ✅ Fix any issues locally
3. ✅ Commit with proper message format
4. ✅ Push to your feature branch

### During PR Review

1. ✅ Ensure all CI/CD checks pass
2. ✅ Address reviewer comments
3. ✅ Keep PR focused and small
4. ✅ Update tests if code changed

### Before Merging

1. ✅ All checks green
2. ✅ At least 1 approval
3. ✅ No merge conflicts
4. ✅ Branch is up to date with base

---

## 🚨 Emergency: Bypassing Checks

**⚠️ Only for critical hotfixes!**

If you absolutely must bypass checks:

1. Contact team lead
2. Explain the emergency
3. Get approval
4. Merge with admin override
5. **Fix issues immediately after**

**Never bypass checks for regular features!**

---

## 📊 Coverage Reports

### Viewing Coverage

After PR checks run:

1. Go to PR on GitHub
2. Click "Actions" tab
3. Find "Test Coverage Report" job
4. Download "coverage-report" artifact
5. Open `htmlcov/index.html` in browser

### Coverage Goals

- **Minimum:** 70% coverage
- **Target:** 80%+ coverage
- **Critical files:** 90%+ coverage

---

## 🔐 Security Scanning

### What's Checked

1. **Dependencies** - Known vulnerabilities in packages
2. **Code patterns** - Insecure code practices
3. **Secrets** - Accidentally committed keys/passwords

### If Security Issues Found

1. Review the security report
2. Update vulnerable packages
3. Fix insecure code patterns
4. Remove any committed secrets
5. Rotate compromised credentials

---

## 🎓 Learning Resources

### Understanding CI/CD
- GitHub Actions: https://docs.github.com/en/actions
- CI/CD Best Practices: https://www.atlassian.com/continuous-delivery

### Code Quality Tools
- Black: https://black.readthedocs.io/
- flake8: https://flake8.pycqa.org/
- pytest: https://docs.pytest.org/

---

## 🆘 Getting Help

### CI/CD Failing?

1. **Check the logs** - Click "Details" on failed check
2. **Run locally** - Use `./run_checks.sh`
3. **Ask team** - Share error message in chat
4. **Check docs** - This file and GitHub Actions docs

### Still Stuck?

- Post in team chat with:
  - Link to failing check
  - Error message
  - What you've tried
  - Your branch name

---

## 📝 Summary

**Automatic on every push:**
- ✅ Tests on 2 OS × 3 Python versions
- ✅ Code quality checks
- ✅ Security scanning

**Automatic on PRs:**
- ✅ PR validation
- ✅ Coverage reports
- ✅ Changed files analysis

**Automatic on main:**
- ✅ Deployment validation
- ✅ Release tagging

**Run locally before pushing:**
```bash
./run_checks.sh  # Linux/Mac
run_checks.bat   # Windows
```

**All checks must pass before merging to main!**

---

**Questions?** Check this guide or ask in team chat! 🚀
