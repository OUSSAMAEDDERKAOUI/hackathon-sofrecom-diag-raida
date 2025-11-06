# Setup Guide

This guide explains how to set up the project on **Windows** and **Linux**.

---

## 1. Clone the Repository
```bash
  git clone <repository_url>
cd hackathon-sofrecom-diag-raida/backend
```
```bash
  python3 -m venv venv
source venv/bin/activate
```
```bash
  python -m venv venv
.\venv\Scripts\activate
```
```bash
  pip install -r requirements.txt
```

Optional: Use Setup Scripts
```bash
  Linux: bash setup.sh
```
```bash
  Windows: setup.bat
```

```bash
  python run.py
```
```bash
  pytest tests/
# or
python -m unittest discover -s tests


