# scripts/deployment/deploy_local.ps1
# This script automates the process of pushing local changes to GitHub 
# and (optionally) triggering a server update.

param (
    [string]$CommitMessage = "Auto-update from local machine",
    [switch]$ForceUpdate = $false
)

# 1. Stage and commit changes
Write-Host "--- Staging and Committing ---" -ForegroundColor Cyan
git add .
if ($LASTEXITCODE -ne 0) { Write-Error "Failed to stage changes"; exit 1 }

# Check if there are changes to commit
$status = git status --porcelain
if (-not $status) {
    Write-Host "No changes to commit." -ForegroundColor Yellow
} else {
    git commit -m $CommitMessage
    if ($LASTEXITCODE -ne 0) { Write-Error "Failed to commit changes"; exit 1 }
}

# 2. Push to GitHub
Write-Host "--- Pushing to GitHub ---" -ForegroundColor Cyan
git push origin main
if ($LASTEXITCODE -ne 0) { Write-Error "Failed to push to GitHub"; exit 1 }

Write-Host "--- Push Complete! ---" -ForegroundColor Green
Write-Host "The GitHub CI/CD pipeline should now trigger automatically." -ForegroundColor Gray
Write-Host "If you have the server_updater.sh running on your server, it will also pick up changes soon." -ForegroundColor Gray
