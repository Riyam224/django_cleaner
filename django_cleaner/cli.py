import argparse
import os
from django_cleaner.cleaner import clean_project, format_size


def is_django_project(path):
    return os.path.exists(os.path.join(path, "manage.py"))


def main():
    parser = argparse.ArgumentParser(
        prog="django-cleaner",
        description="🧹 Clean multiple Django projects (migrations, cache, etc.)",
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path containing Django projects (default: current directory)",
    )

    parser.add_argument(
        "--venv",
        action="store_true",
        help="Delete virtual environments (venv) without confirmation",
    )

    args = parser.parse_args()

    base_path = os.path.expanduser(args.path)

    # ✅ Validate path
    if not os.path.exists(base_path):
        print(f"❌ Path does not exist: {base_path}")
        return

    # ✅ Handle venv deletion
    remove_venv = args.venv

    if not remove_venv:
        confirm = (
            input("⚠️ Do you want to delete virtual environments (venv)? (y/n): ")
            .strip()
            .lower()
        )
        remove_venv = confirm == "y"

    print("\n🚀 Starting cleanup...\n")

    found_projects = False
    total_all = 0

    for folder in os.listdir(base_path):
        if folder.startswith("."):
            continue

        full_path = os.path.join(base_path, folder)

        if os.path.isdir(full_path) and is_django_project(full_path):
            found_projects = True

            freed = clean_project(full_path, remove_venv)
            total_all += freed

    if not found_projects:
        print("⚠️ No Django projects found in this directory.")
    else:
        print(f"\n🚀 Total space freed: {format_size(total_all)}")
        print("\n🎉 All projects cleaned successfully!")


if __name__ == "__main__":
    main()
