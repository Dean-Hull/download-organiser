from pathlib import Path

from file_categories import get_category

downloads = Path.home() / "Downloads"

for item in downloads.iterdir():
    if item.is_file():
        category = get_category(item)
        print(item.name, category)