import os
import shutil


def get_size(path):
    total = 0
    if os.path.exists(path):
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total += os.path.getsize(fp)
    return total


def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"


def delete_folder(path):
    size = get_size(path)
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"🗑 Deleted: {path} ({format_size(size)})")
    return size


def delete_files(root, extension):
    total = 0
    for dirpath, _, filenames in os.walk(root):
        for file in filenames:
            if file.endswith(extension):
                file_path = os.path.join(dirpath, file)
                size = os.path.getsize(file_path)
                os.remove(file_path)
                total += size
                print(f"🗑 Deleted file: {file_path} ({format_size(size)})")
    return total


def clean_project(project_path, remove_venv=False):
    print(f"\n🧹 Cleaning: {project_path}")

    total_freed = 0

    for root, dirs, _ in os.walk(project_path):

        if "__pycache__" in dirs:
            total_freed += delete_folder(os.path.join(root, "__pycache__"))

        if "logs" in dirs:
            total_freed += delete_folder(os.path.join(root, "logs"))

        if "staticfiles" in dirs:
            total_freed += delete_folder(os.path.join(root, "staticfiles"))

    total_freed += delete_files(project_path, ".pyc")

    if remove_venv:
        total_freed += delete_folder(os.path.join(project_path, "venv"))

    print(f"✨ Freed: {format_size(total_freed)} from {project_path}")
    return total_freed
