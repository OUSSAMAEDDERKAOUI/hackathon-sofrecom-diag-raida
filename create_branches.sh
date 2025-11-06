#!/bin/bash
# Script to create all feature branches from main

echo "🌿 Creating Feature Branches"
echo "=============================="
echo ""

# Make sure we're on main and up to date
echo "📍 Checking out main branch..."
git checkout main

echo "📥 Pulling latest changes..."
git pull origin main

echo ""
echo "🌿 Creating feature branches..."
echo ""

# Array of feature branches
branches=(
    "feature/llm-integration"
    "feature/data-structures"
    "feature/analysis-service"
    "feature/evaluation-service"
    "feature/recommendation-service"
    "feature/ml-models"
)

# Create each branch
for branch in "${branches[@]}"; do
    echo "Creating $branch..."
    git checkout -b "$branch" 2>/dev/null || git checkout "$branch"
    git push -u origin "$branch" 2>/dev/null || echo "  (branch already exists on remote)"
    echo "  ✅ $branch ready"
    echo ""
done

# Go back to main
echo "📍 Returning to main branch..."
git checkout main

echo ""
echo "=============================="
echo "✅ All feature branches created!"
echo "=============================="
echo ""
echo "Available branches:"
git branch -a | grep feature/

echo ""
echo "📋 Next steps:"
echo "1. Assign team members to branches (see FEATURE_BRANCHES.md)"
echo "2. Each member: git checkout feature/their-branch"
echo "3. Start coding!"
echo ""
