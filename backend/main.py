from pathlib import Path

from scan import scan_folder

downloads = Path.home() / "Downloads"
files = scan_folder(downloads)

for file in files:
    print(file)