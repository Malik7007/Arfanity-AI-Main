# 🚀 Automated Deployment Guide

This guide explains how to use the included scripts to keep your server up-to-date with your local changes automatically.

## 🚀 Getting Started

### 1. How to update from Local Machine
Whenever you make changes to the code, open PowerShell in the project root and run:

```powershell
.\scripts\deployment\deploy_local.ps1 -CommitMessage "Improved the UI"
```

### 2. How to set up Auto-Update on the Server
On your server (where Docker is running), you can start the auto-updater script.

> [!IMPORTANT]
> This script assumes you have cloned the repository on your server. It will use the main `docker-compose.yml` (which builds from source) rather than the `deploy/docker-compose.server.yml` (which pulls pre-built images).

1.  Navigate to the project directory on the server.
2.  Make the script executable:
    ```bash
    chmod +x scripts/deployment/server_updater.sh
    ```
3.  Run it inside a `screen` session:
    ```bash
    screen -S arfanity-update ./scripts/deployment/server_updater.sh 60
    ```
    *(The `60` means it checks every 60 seconds)*

### Option B: Run as a Systemd Service (Recommended for Stability)
Create a file `/etc/systemd/system/arfanity-update.service`:

```ini
[Unit]
Description=Arfanity AI Auto-Updater
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/Arfanity-AI-main
ExecStart=/bin/bash /path/to/Arfanity-AI-main/scripts/deployment/server_updater.sh 60
Restart=always

[Install]
WantedBy=multi-user.target
```

Then enable and start it:
```bash
sudo systemctl enable arfanity-update
sudo systemctl start arfanity-update
```

---

## 🔗 Using GitHub Actions (Optional)

The repo also includes a production-grade CI/CD pipeline in `.github/workflows/docker-ci-cd.yml`. 

**When to use this instead?**
-   If you don't want to keep source code on the server.
-   If you want to use GitHub's build servers instead of your own.
-   If you have a public-facing server.

Refer to the main `README.md` for setup instructions for GitHub Actions.
