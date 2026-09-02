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