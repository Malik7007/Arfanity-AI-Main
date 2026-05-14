#!/bin/bash
# scripts/deployment/server_updater.sh
# Run this script on your server to automatically pull changes and rebuild Docker containers.
# Usage: ./server_updater.sh [interval_in_seconds]
# Example: ./server_updater.sh 60

INTERVAL=${1:-60} # Default to 60 seconds
PROJECT_DIR=$(pwd)

echo "--- Arfanity AI Server Auto-Updater Started ---"
echo "Project Directory: $PROJECT_DIR"
echo "Polling Interval: $INTERVAL seconds"

while true; do
    echo "$(date): Checking for updates..."
    
    # Fetch latest changes without merging
    git fetch origin main
    
    # Compare local branch with remote
    LOCAL=$(git rev-parse HEAD)
    REMOTE=$(git rev-parse @{u})
    
    if [ "$LOCAL" != "$REMOTE" ]; then
        echo "$(date): New changes detected! Updating..."
        
        # Pull latest changes
        git pull origin main
        
        # Rebuild and restart docker containers
        # We use --build to ensure any code changes are reflected in the image
        docker compose up -d --build
        
        # Clean up old images to save space
        docker image prune -f
        
        echo "$(date): Update complete!"
    else
        echo "$(date): No changes found."
    fi
    
    sleep $INTERVAL
done
