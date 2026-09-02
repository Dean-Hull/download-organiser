from pathlib import Path

from scan import create_summary, group_files, organise_files, scan_folder
from utils import format_size

downloads = Path.home() / "Downloads"
files = scan_folder(downloads)
grouped = group_files(files)
summary = create_summary(files, grouped)

print(
    f"Downloads: "
    f"{summary['total_files']} files: "
    f"{format_size(summary['total_size'])}"
)

for category, years in grouped.items():
    print()
    print(category)

    for year in sorted(years, reverse=True):
        data = years[year]

        print(
            f"{year}: "
            f"{data['count']} files, "
            f"{format_size(data['size'])}"
        )

print()
print("Planned changes:")
organise_files(files, downloads, dry_run=False)
