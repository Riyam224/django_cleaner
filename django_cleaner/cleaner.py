import os
import shutil


def get_size(path):
    """Calculate total size of a file or folder"""
    total = 0

    if not os.path.exists(path):
        return 0

    if os.path.isfile(path):
        return os.path.getsize(path)

    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total += os.path.getsize(fp)

    return total


def format_size(size):
    """Convert bytes to human readable format"""
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"


def delete_folder(path):
    """Delete folder safely and return freed size"""
    size = get_size(path)

    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
        print(f"🗑 Deleted: {os.path.basename(path)} ({format_size(size)})")

    return size


def delete_files(root, extension):
    """Delete files by extension (e.g. .pyc)"""
    total = 0

    for dirpath, _, filenames in os.walk(root):
        for file in filenames:
            if file.endswith(extension):
                file_path = os.path.join(dirpath, file)

                if os.path.exists(file_path):
                    size = os.path.getsize(file_path)
                    os.remove(file_path)
                    total += size

                    print(f"🗑 Deleted file: {file} ({format_size(size)})")

    return total


def clean_project(project_path, remove_venv=False):
    """Clean a single Django project"""
    print(f"\n🧹 Cleaning: {project_path}")

    total_freed = 0

    # 🎯 Target folders to remove
    targets = ["__pycache__", "logs", "staticfiles"]

    for root, dirs, _ in os.walk(project_path):

        for target in targets:
            if target in dirs:
                full_path = os.path.join(root, target)
                total_freed += delete_folder(full_path)

    # 🧹 Remove .pyc files
    total_freed += delete_files(project_path, ".pyc")

    # ⚡ Optional: remove venv
    if remove_venv:
        venv_path = os.path.join(project_path, "venv")
        total_freed += delete_folder(venv_path)

    print(f"✨ Freed: {format_size(total_freed)} from {os.path.basename(project_path)}")

    return total_freed
