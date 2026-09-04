from datetime import datetime
from pathlib import Path

from file_categories import get_file_categories

def scan_folder(folder: Path):
    files = []

    for item in folder.iterdir():
        if not item.is_file():
            continue

        stat = item.stat()
        modified = datetime.fromtimestamp(stat.st_mtime)

        file = {
            "name": item.name,
            "path": str(item),
            "extension": item.suffix.lower(),
            "category": get_file_categories(item),
            "size": stat.st_size,
            "modified": modified,
            "year": modified.year,
            "month": modified.strftime("%m-%B"),
        }

        files.append(file)

    return files


def group_files(files):
    grouped = {}

    for file in files:
        category = file["category"]
        year = file["year"]

        if category not in grouped:
            grouped[category] = {}

        if year not in grouped[category]:
            grouped[category][year] = {
                "count": 0,
                "size": 0,
                "files": [],
            }

        grouped[category][year]["count"] += 1
        grouped[category][year]["size"] += file["size"]
        grouped[category][year]["files"].append(file)

    return grouped


def create_summary(files, grouped):
    total_size = sum(file["size"] for file in files)

    return {
        "total_files": len(files),
        "total_size": total_size,
        "groups": grouped
    }


def organise_files(files, root: Path, dry_run: bool = True):
    for file in files:
        source = Path(file["path"])

        destination_folder = (
            root / file["category"] / str(file["year"]) / file["month"]
        )

        destination = destination_folder / source.name

        if destination.exists():
            print(f"Skipped: {source.name} already exists")
            continue

        if dry_run:
            print(f"Would move: {source} -> {destination}")
            continue

        destination_folder.mkdir(parents=True, exist_ok=True)
        source.rename(destination)

        print(f"Moved: {source.name} -> {destination_folder}")

def migrate_existing_files(root: Path, dry_run: bool = True,):
    categories = {
        "Archives",
        "Audio",
        "Documents",
        "Images",
        "Installers",
        "Other",
        "Videos",
    }
    
    for category in categories:
        category_folder = root / category
        
        if not category_folder.exists():
            continue
        
        for year_folder in category_folder.iterdir():
            if not year_folder.is_dir():
                continue
            
            if not year_folder.name.isdigit():
                continue
            
            if len(year_folder.name) != 4:
                continue
            
            for source in year_folder.iterdir():
                if not source.is_file():
                    continue
                
                modified = datetime.fromtimestamp(source.stat().st_mtime)
                
                month = modified.strftime("%m-%B")
                destination_folder = year_folder / month
                destination = destination_folder / source.name
                
                if destination.exists():
                    print(f"Skipped existing file: " f"{destination}")
                    continue
                
                if dry_run:
                    print(f"Would migrate: " f"{source} -> {destination}")
                    continue
                
                destination_folder.mkdir(parents=True, exist_ok=True)
                
                source.rename(destination)
                
                print(f"Migrated: " f"{source} -> {destination}")
                
