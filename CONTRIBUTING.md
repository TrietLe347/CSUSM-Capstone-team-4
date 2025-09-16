# Contributing to PoseMirror
```bash
Welcome to our Capstone group project! 🎉  
This guide explains how we’ll work together, keep things organized, and make sure everyone is on the same page.
```
---

## 🚀 Getting Started

## 1. **Clone the repo**
   ```bash
   git clone https://github.com/<username>/<repo>.git
   cd <repo>
```
## 2. Set up your Python environment
```bash

# Windows
py -3.10 -m venv .venv
.\.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```
## 3. Install dependencies

```bash

pip install -r requirements.txt
```

## 4. Test it
```bash

python verify_pose.py
```
→ You should see your webcam with a skeleton overlay.

## 🌱 How We Use GitHub
The main branch always has code that runs.

Do your work on a new branch. Example:

```bash

git checkout -b feat/unity-bridge
```

When you’re done, push your branch and open a Pull Request (PR).

A teammate reviews it, then we merge into main.
---
## 📝 Commit Messages
Keep commits short and clear. For example:

feat: add MediaPipe backend

fix: release camera after exit

docs: update README setup steps

## 🔄 Pull Requests
When you open a PR:

Describe what you changed and why.

If it affects how the program runs, add test steps (how we can check it).

One teammate should review before merging.

## 📂 Project Structure
```bash
src/
  pose/        # code for pose detection
  bridge/      # code for WebSocket/Unity connection
main.py        # main entry point
verify_pose.py # quick webcam test
```
## ⚡ Coding Guidelines
Use Python 3.10 (works best with our libraries).

Keep functions small and readable.

Don’t commit secrets (API keys, .env files, etc).

Keep dependencies in requirements.txt up to date.

## 👥 Team Workflow
Weekly check-ins with our mentor (Time TBD).

Discord/Teams for quick questions.

Use GitHub Issues to track bugs, features, or tasks.

## 🎯 Goals
Get a simple baseline working first (MediaPipe skeleton).

Replace with Qualcomm AI Hub models once hardware is ready.

Add animation (Unity/WebGL) and split-screen UI.

## ✅ Quick Checklist Before You Commit
Code runs without crashing.

No random files committed (.venv/, .idea/, cache files).

Update docs if something important changed.

Thanks for contributing and let’s build something awesome together! 🙌
