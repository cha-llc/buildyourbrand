#!/usr/bin/env python3
"""
buildyourbrand Automated Deployment Script
Deploys multilingual portfolio to GitHub and Vercel
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a shell command and report results"""
    print(f"\n{'='*70}")
    print(f"▶ {description}")
    print(f"{'='*70}")
    print(f"$ {cmd}\n")
    
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"✗ Failed: {description}")
        return False
    print(f"✓ Completed: {description}")
    return True

def main():
    print("""
╔════════════════════════════════════════════════════════════════════╗
║          BUILD YOUR BRAND — AUTOMATED DEPLOYMENT SCRIPT           ║
║                     Multilingual Portfolio v1.0                    ║
╚════════════════════════════════════════════════════════════════════╝
    """)
    
    # Check prerequisites
    print("Checking prerequisites...")
    
    if subprocess.run("which gh > /dev/null 2>&1", shell=True).returncode != 0:
        print("✗ GitHub CLI not found. Install: https://cli.github.com")
        return
    print("✓ GitHub CLI found")
    
    if subprocess.run("which git > /dev/null 2>&1", shell=True).returncode != 0:
        print("✗ Git not found. Install: https://git-scm.com")
        return
    print("✓ Git found")
    
    # Get username
    result = subprocess.run("gh api user -q .login 2>/dev/null", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("✗ Not authenticated with GitHub. Run: gh auth login")
        return
    
    username = result.stdout.strip()
    print(f"✓ Authenticated as: {username}")
    
    # Initialize git repo
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    commands = [
        ("git init", "Initialize git repository"),
        ("git config user.email 'build@yourbrand.app'", "Configure git email"),
        ("git config user.name 'Build Your Brand'", "Configure git name"),
        ("git add .", "Stage files"),
        ("git commit -m 'Initial deployment: multilingual TikTok branding portfolio with 15 languages' --allow-empty", "Commit files"),
        ("git branch -M main", "Rename branch to main"),
    ]
    
    for cmd, desc in commands:
        if not run_command(cmd, desc):
            print(f"\n✗ Deployment failed at: {desc}")
            return
    
    # Create GitHub repo
    print(f"\n{'='*70}")
    print(f"▶ Creating GitHub repository...")
    print(f"{'='*70}\n")
    
    result = subprocess.run(
        f"gh repo create buildyourbrand --public --source=. --remote=origin --push",
        shell=True
    )
    
    if result.returncode != 0:
        print("\n⚠ Repository may already exist. Attempting to push to existing repo...")
        subprocess.run("git remote add origin https://github.com/{}/buildyourbrand.git 2>/dev/null || git remote set-url origin https://github.com/{}/buildyourbrand.git".format(username, username), shell=True)
        subprocess.run("git push -u origin main", shell=True)
    
    print("\n" + "="*70)
    print("✓ DEPLOYMENT COMPLETE")
    print("="*70)
    print(f"""
Repository: https://github.com/{username}/buildyourbrand
Status: Ready for Vercel deployment

NEXT STEPS:
───────────────────────────────────────────────────────────────────────

1. Go to: https://vercel.com/new
2. Click: "Import Git Repository"
3. Paste: https://github.com/{username}/buildyourbrand
4. Click: "Import" then "Deploy"
5. Wait 30 seconds...
6. Your site: https://buildyourbrand.vercel.app

DONE IN 2 MINUTES

═══════════════════════════════════════════════════════════════════════════
    """)

if __name__ == "__main__":
    main()
