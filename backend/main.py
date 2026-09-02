from pathlib import Path

from scan import group_files, scan_folder

downloads = Path.home() / "Downloads"
files = scan_folder(downloads)
grouped = group_files(files)

for category, years in grouped.items():
    print()
    print(category)
    
    for year, data in years.items():
        print(
            f"{year}: "
            f"{data['count']} files, "
            f"{data['size']} bytes"
        )