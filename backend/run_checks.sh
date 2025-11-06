#!/bin/bash
# Local code quality checks - run before committing

echo "🔍 Running code quality checks..."
echo ""

# Activate venv if not already active
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

cd "$(dirname "$0")"

# Track if any checks fail
FAILED=0

# 1. Format check with Black
echo "1️⃣ Checking code formatting (Black)..."
if black --check app tests 2>/dev/null; then
    echo "   ✅ Code formatting is correct"
else
    echo "   ❌ Code formatting issues found"
    echo "   Fix with: black app tests"
    FAILED=1
fi
echo ""

# 2. Import sorting check
echo "2️⃣ Checking import sorting (isort)..."
if isort --check-only app tests 2>/dev/null; then
    echo "   ✅ Imports are sorted correctly"
else
    echo "   ❌ Import sorting issues found"
    echo "   Fix with: isort app tests"
    FAILED=1
fi
echo ""

# 3. Linting with flake8
echo "3️⃣ Linting code (flake8)..."
if flake8 app tests 2>/dev/null; then
    echo "   ✅ No linting issues"
else
    echo "   ⚠️  Linting issues found (see above)"
    FAILED=1
fi
echo ""

# 4. Run tests
echo "4️⃣ Running tests (pytest)..."
if pytest tests/ -v --tb=short; then
    echo "   ✅ All tests passed"
else
    echo "   ❌ Tests failed"
    FAILED=1
fi
echo ""

# 5. Security check
echo "5️⃣ Security scan (bandit)..."
if bandit -r app -q 2>/dev/null; then
    echo "   ✅ No security issues found"
else
    echo "   ⚠️  Security issues found (see above)"
    # Don't fail on security warnings, just notify
fi
echo ""

# Summary
echo "================================"
if [ $FAILED -eq 0 ]; then
    echo "✅ All checks passed! Safe to commit."
    exit 0
else
    echo "❌ Some checks failed. Please fix before committing."
    exit 1
fi
