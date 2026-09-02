from datetime import datetime
from pathlib import Path

from file_categories import get_file_categories

def scan_folder(folder: Path):
    files = []
    
    for item in folder.iterdir():
        if not item.is_file():
            continue
        
        stat = item.stat()
        
        file = {
            "name": item.name,
            "path": str(item),
            "extension": item.suffix.lower(),
            "category": get_file_categories(item),
            "size": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime),
            "year": datetime.fromtimestamp(stat.st_mtime).year
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