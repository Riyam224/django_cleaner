from setuptools import setup, find_packages

setup(
    name="django-cleaner",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "django-cleaner=django_cleaner.cli:main",
        ],
    },
    author="Riyam",
    description="CLI tool to clean Django projects safely",
)
