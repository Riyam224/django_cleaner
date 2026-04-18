# 🧹 Django Cleaner

<p align="center">
  <b>Clean your Django projects in seconds ⚡</b><br>
  Remove cache, logs, and junk safely — without touching your code 💙
</p>

<p align="center">
  🔗 <a href="https://pypi.org/project/django-cleaner/">PyPI</a> •
  📦 <code>pip install django-cleaner</code>
</p>

---

<p align="center">
  <img src="https://img.shields.io/pypi/v/django-cleaner">
  <img src="https://img.shields.io/pypi/pyversions/django-cleaner">
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey">
  <img src="https://img.shields.io/badge/license-MIT-green">
</p>

---

## ✨ Features

- 🗑 Remove `__pycache__` folders  
- 🗑 Remove `.pyc` files  
- 🗑 Remove `logs/`  
- 🗑 Remove `staticfiles/`  
- ⚡ Optional removal of `venv/`  
- 🔍 Automatically detects Django projects  
- 💾 Shows how much space was freed  

---

## 🎥 Example

```bash
django-cleaner ~/StudioProjects
```

```text
🧹 Cleaning: my_project
🗑 Deleted: __pycache__ (2.3 MB)
🗑 Deleted: venv (350 MB)

✨ Freed: 352.3 MB from my_project

🚀 Total space freed: 1.2 GB
🎉 All projects cleaned successfully!
```

---

## 📦 Installation

### 🔹 Using pipx (Recommended)

```bash
brew install pipx
pipx ensurepath
pipx install django-cleaner
```

### 🔹 Using pip

```bash
pip install django-cleaner
```

---

## 🚀 Usage

### Clean current directory

```bash
django-cleaner
```

### Clean specific directory

```bash
django-cleaner ~/StudioProjects
```

### Skip confirmation (auto delete venv)

```bash
django-cleaner ~/StudioProjects --venv
```

---

## ⚠️ Prompt

```text
Do you want to delete virtual environments (venv)? (y/n)
```

---

## 🧠 What gets cleaned?

| Item           | Safe            |
|----------------|-----------------|
| `__pycache__`  | ✅ Yes          |
| `.pyc` files   | ✅ Yes          |
| `logs/`        | ✅ Yes          |
| `staticfiles/` | ✅ Yes          |
| `venv/`        | ⚠️ Optional     |

---

## 🚫 What is NOT deleted?

- Your Django code  
- `manage.py`  
- apps (`models.py`, `views.py`, etc.)  
- database files  

👉 Your project remains fully usable

---

## 🔁 After Cleaning

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🌍 Supported Systems

- macOS ✅  
- Linux ✅  
- Windows ⚠️ (may need minor adjustments)

---

## 💡 Why this tool?

Django projects accumulate hidden junk over time:

- cache files  
- compiled Python files  
- unused environments  

👉 This tool keeps your machine clean and fast ⚡

---

## 🚀 Roadmap

- [ ] `--dry-run` mode 👀  
- [ ] Windows full support  
- [ ] Multi-command CLI (clean / scan / report)

---

## ❤️ Author

Built by **Riyam** ✨  
Flutter & Django Developer  

---

## ⭐ Support

If you like this project, give it a star ⭐  
It helps a lot 💙
