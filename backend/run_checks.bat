@echo off
REM Local code quality checks - run before committing (Windows)

echo 🔍 Running code quality checks...
echo.

REM Activate venv if not already active
if not defined VIRTUAL_ENV (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

cd /d "%~dp0"

REM Track if any checks fail
set FAILED=0

REM 1. Format check with Black
echo 1️⃣ Checking code formatting (Black)...
black --check app tests 2>nul
if %ERRORLEVEL% EQU 0 (
    echo    ✅ Code formatting is correct
) else (
    echo    ❌ Code formatting issues found
    echo    Fix with: black app tests
    set FAILED=1
)
echo.

REM 2. Import sorting check
echo 2️⃣ Checking import sorting (isort)...
isort --check-only app tests 2>nul
if %ERRORLEVEL% EQU 0 (
    echo    ✅ Imports are sorted correctly
) else (
    echo    ❌ Import sorting issues found
    echo    Fix with: isort app tests
    set FAILED=1
)
echo.

REM 3. Linting with flake8
echo 3️⃣ Linting code (flake8)...
flake8 app tests 2>nul
if %ERRORLEVEL% EQU 0 (
    echo    ✅ No linting issues
) else (
    echo    ⚠️  Linting issues found
    set FAILED=1
)
echo.

REM 4. Run tests
echo 4️⃣ Running tests (pytest)...
pytest tests\ -v --tb=short
if %ERRORLEVEL% EQU 0 (
    echo    ✅ All tests passed
) else (
    echo    ❌ Tests failed
    set FAILED=1
)
echo.

REM 5. Security check
echo 5️⃣ Security scan (bandit)...
bandit -r app -q 2>nul
if %ERRORLEVEL% EQU 0 (
    echo    ✅ No security issues found
) else (
    echo    ⚠️  Security issues found
)
echo.

REM Summary
echo ================================
if %FAILED% EQU 0 (
    echo ✅ All checks passed! Safe to commit.
    exit /b 0
) else (
    echo ❌ Some checks failed. Please fix before committing.
    exit /b 1
)
