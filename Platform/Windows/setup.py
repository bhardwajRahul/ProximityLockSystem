from setuptools import setup, find_packages

import os

readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if not os.path.exists(readme_path):
    readme_path = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")

long_description = ""
if os.path.exists(readme_path):
    with open(readme_path, encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="proximity-lock-system",
    version="2.1.0",
    packages=find_packages(),
    install_requires=[
        "pybluez"
    ],
    entry_points={
        "console_scripts": [
            "proximity-lock=proximity_lock_system.cli:main",
        ],
    },
    author="Akarsh Jha",
    description="Security-style CLI that locks your system when your phone leaves Bluetooth range.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Akarshjha03/ProximityLockSystem",
    python_requires=">=3.8",
)
