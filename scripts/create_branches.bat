@echo off
REM Script to create all feature branches from main

echo 🌿 Creating Feature Branches
echo ==============================
echo.

REM Make sure we're on main and up to date
echo 📍 Checking out main branch...
git checkout main

echo 📥 Pulling latest changes...
git pull origin main

echo.
echo 🌿 Creating feature branches...
echo.

REM Create each branch
call :create_branch feature/llm-integration
call :create_branch feature/data-structures
call :create_branch feature/analysis-service
call :create_branch feature/evaluation-service
call :create_branch feature/recommendation-service
call :create_branch feature/ml-models

REM Go back to main
echo 📍 Returning to main branch...
git checkout main

echo.
echo ==============================
echo ✅ All feature branches created!
echo ==============================
echo.
echo Available branches:
git branch -a | findstr feature/

echo.
echo 📋 Next steps:
echo 1. Assign team members to branches (see FEATURE_BRANCHES.md)
echo 2. Each member: git checkout feature/their-branch
echo 3. Start coding!
echo.

goto :eof

:create_branch
echo Creating %1...
git checkout -b %1 2>nul || git checkout %1
git push -u origin %1 2>nul || echo   (branch already exists on remote)
echo   ✅ %1 ready
echo.
goto :eof
