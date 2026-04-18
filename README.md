
````markdown
# 🧹 Django Cleaner

<p align="center">
  <b>Clean your Django projects in seconds ⚡</b><br>
  Remove cache, logs, and junk safely — without touching your code 💙
</p>

<p align="center">
  🔗 <a href="https://pypi.org/project/django-cleaner/">View on PyPI</a> •
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

## 🎬 Demo

<p align="center">
  <img src="assets/demo.gif" width="700">
</p>

---

## ✨ Features

- 🗑 Remove `__pycache__` folders  
- 🗑 Remove `.pyc` files  
- 🗑 Remove `logs/` directories  
- 🗑 Remove `staticfiles/` (collected static)  
- ⚡ Optional removal of `venv/`  
- 🔍 Automatically detects Django projects (`manage.py`)  
- 💾 Displays total freed disk space  

---

## ⚡ Quick Example

```bash
django-cleaner ~/StudioProjects
````

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

### 🔹 Using pipx (Recommended for CLI tools)

```bash
brew install pipx
pipx ensurepath
pipx install django-cleaner
```

👉 Installs the tool globally in an isolated environment (no dependency conflicts)

---

### 🔹 Using pip

```bash
pip install django-cleaner
```

---

### 🔹 From source (GitHub)

```bash
git clone https://github.com/your-username/django-cleaner.git
cd django-cleaner
pip install .
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

### Auto-delete virtual environments

```bash
django-cleaner ~/StudioProjects --venv
```

---

## ⚠️ Important Notes

### ❗ If installed with pip:

Make sure you're **not inside a virtual environment** before running:

```bash
deactivate
```

👉 This prevents accidental deletion of the active `venv`

---

## 🧠 What gets cleaned?

| Item           | Safe        |
| -------------- | ----------- |
| `__pycache__`  | ✅ Yes       |
| `.pyc` files   | ✅ Yes       |
| `logs/`        | ✅ Yes       |
| `staticfiles/` | ✅ Yes       |
| `venv/`        | ⚠️ Optional |

---

## 🚫 What is NOT deleted?

* Django source code
* `manage.py`
* apps (`models.py`, `views.py`, etc.)
* database files

👉 Your project remains fully functional

---

## 🔁 After Cleaning (if venv removed)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🌍 Supported Systems

* macOS ✅
* Linux ✅
* Windows ⚠️ (basic support)

---

## 💡 Why this tool?

Django projects accumulate unnecessary files over time:

* cache folders
* compiled `.pyc` files
* unused virtual environments

👉 This tool helps you reclaim disk space and keep your workspace clean ⚡

---

## 🚀 Roadmap

* [ ] `--dry-run` mode (preview changes)
* [ ] Progress bar support
* [ ] Improved Windows compatibility
* [ ] Advanced filtering options

---

## ❤️ Author

Built by **Riyam** ✨
Flutter & Django Developer

---

## ⭐ Support

If this project helped you:

⭐ Star the repo
📦 Share it with other developers

It really helps 💙

````

---

# 🎥 How to record the GIF (quick pro tip)

Use one of these:

- **Mac:** QuickTime + convert to GIF (ezgif.com)
- **Best tool:** Screen Studio (super smooth)
- **Free:** Kap

👉 Record this flow:

```bash
django-cleaner ~/Projects
→ show deleting
→ show final result
````

Keep it **5–8 seconds max** → looks professional ✨

---

# 😏 Final touch (important)

After adding GIF:

```bash
git add assets/demo.gif
git commit -m "Add demo GIF"
git push
```

---


