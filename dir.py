import os

# Directories to create
dirs = [
    ".github/workflows",
    "tests"
]

# Files to create
files = [
    ".github/workflows/ci-cd.yml",
    "tests/test_app.py",
    "app.py",
    "requirements.txt",
    ".gitignore",
    "README.md"
]

# Create directories
for dir_path in dirs:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Directory created: {dir_path}")
    else:
        print(f"Directory already exists: {dir_path}")

# Create files
for file_path in files:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass  # Simply create an empty file
        print(f"File created: {file_path}")
    else:
        print(f"File already exists: {file_path}")
dir 