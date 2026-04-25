# 🌌 Arfanity AI

![Arfanity AI Banner](https://github.com/Malik7007/Arfanity-AI-Main/raw/main/static/favicon.png)

**Arfanity AI** is a premium, high-performance AI user interface designed for seamless interaction with Large Language Models. Built for author **Arfan Malik**, it provides a state-of-the-art, "Advanced UI" experience for individuals and enterprises looking to leverage AI in their daily workflows.

---

## ✨ Features

### 💎 Advanced UI System
- **Glassmorphism Design**: High-end backdrop blurs, translucent borders, and radial glow effects.
- **Dynamic Themes**: Strictly enforced Light/Dark modes for regular users, with a full theme suite for Administrators.
- **Premium Animations**: Staggered message entry, floating glass input islands, and micro-interactions.
- **Arabic (RTL) Support**: Full Right-to-Left layout support for Arabic speakers, featuring automatic sidebar mirroring.

### 🤖 Intelligent Model Management
- **Multi-Model Integration**: Connect to Ollama, OpenAI, Anthropic, Gemini, and more.
- **Smart Model Selector**: Automatically adjusts between a dropdown and a clean label based on user permissions.
- **Pinned Models**: Quickly access your most-used models from the sidebar.

### 📁 Advanced Workspace
- **RAG Support**: Retrieval-Augmented Generation with local and cloud storage.
- **Folder Management**: Organize chats into custom folders with nested hierarchies.
- **Temporary Chats**: Incognito mode for private, non-persisted conversations.

### 🛡️ Enterprise Security
- **Role-Based Access Control (RBAC)**: Granular permissions for Users and Admins.
- **Private Deployment**: Deploy locally or on your own servers with Docker.
- **Secure Storage**: Your data stays under your control at all times.

---

## 🚀 Getting Started

### Prerequisites
- **Node.js**: `v18+`
- **Python**: `v3.11+`
- **Docker** (Optional for production)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Malik7007/Arfanity-AI-Main.git
   cd Arfanity-AI-Main
   ```

2. **Setup Backend**:
   ```bash
   cd backend
   # Create a virtual environment
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. **Setup Frontend**:
   ```bash
   cd ..
   npm install
   ```

### Running the Application

1. **Start the Backend**:
   ```bash
   cd backend
   ./start_windows.bat  # Windows
   # OR
   ./start.sh          # Linux/macOS
   ```

2. **Start the Frontend**:
   ```bash
   npm run dev
   ```

3. **Access the App**:
   - Frontend: `http://localhost:5173`
   - Backend API: `http://localhost:8080`

---

## 🐳 Docker Deployment

For a quick production-ready deployment:

```bash
docker compose up -d --build
```

---

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👑 Credits

Developed and Maintained by **Arfan Malik** ([Malik7007](https://github.com/Malik7007))

© 2026 Arfan Malik. All rights reserved.
