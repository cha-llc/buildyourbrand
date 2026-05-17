#!/bin/bash

# buildyourbrand AUTOMATED DEPLOYMENT SCRIPT
# This script will:
# 1. Create a GitHub repo
# 2. Push files to GitHub
# 3. Deploy to Vercel
# 
# Requirements:
# - GitHub account (https://github.com)
# - Git installed (git --version)
# - GitHub CLI installed (https://cli.github.com)
# - Vercel account (https://vercel.com)
# 
# SETUP:
# 1. Install GitHub CLI: https://cli.github.com
# 2. Run: gh auth login
# 3. Run this script: bash deploy.sh

set -e

echo "════════════════════════════════════════════════════════════════"
echo "BUILDYOURBRAND DEPLOYMENT SCRIPT"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Check if gh (GitHub CLI) is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI not found. Install it: https://cli.github.com"
    exit 1
fi

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Install it: https://git-scm.com"
    exit 1
fi

# Get GitHub username
echo "Getting your GitHub username..."
GITHUB_USER=$(gh api user -q .login)
echo "✓ Logged in as: $GITHUB_USER"
echo ""

# Create GitHub repo
echo "Creating GitHub repository..."
REPO_URL="https://github.com/$GITHUB_USER/buildyourbrand"
gh repo create buildyourbrand --public --source=. --remote=origin --push 2>/dev/null || echo "Repository may already exist, skipping creation"
echo "✓ Repository: $REPO_URL"
echo ""

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git config user.email "build@yourbrand.app"
    git config user.name "Build Your Brand"
fi

# Add files
echo "Adding files to git..."
git add .
git commit -m "Initial deployment: multilingual TikTok branding portfolio with 15 languages" --allow-empty
git branch -M main
echo "✓ Files committed"
echo ""

# Push to GitHub
echo "Pushing to GitHub..."
git remote add origin "https://github.com/$GITHUB_USER/buildyourbrand.git" 2>/dev/null || git remote set-url origin "https://github.com/$GITHUB_USER/buildyourbrand.git"
git push -u origin main
echo "✓ Pushed to GitHub"
echo ""

# Deploy to Vercel
echo "════════════════════════════════════════════════════════════════"
echo "NEXT: DEPLOY TO VERCEL"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "1. Go to: https://vercel.com/new"
echo "2. Click: 'Import Git Repository'"
echo "3. Paste: $REPO_URL"
echo "4. Click: 'Import'"
echo "5. Click: 'Deploy'"
echo ""
echo "Vercel will automatically deploy your site in ~30 seconds."
echo ""
echo "Your live site: https://buildyourbrand.vercel.app"
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""
