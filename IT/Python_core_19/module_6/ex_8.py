"""
Створення директорій pathlib
"""
from pathlib import Path
new_dir = Path('Hello')
new_dir.mkdir(exist_ok=True)
new_dir.rmdir()
new_dir = Path('Hello/world/test')
new_dir.mkdir(exist_ok=True, parents=True)