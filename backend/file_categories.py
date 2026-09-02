from pathlib import Path

FILE_TYPES = {
    "Documents": {
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".xls",
        ".ppt",
        ".pptx",
        ".csv"
    },
    "Images": {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".svg",
    },
    "Videos": {
        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
        ".webm",
    },
    "Audio": {
        ".mp3",
        ".wav",
        ".flac",
        ".aac",
        ".m4a",
    },
    "Archives": {
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
    },
    "Installers": {
        ".exe",
        ".msi",
    }
}

def get_file_categories(file: Path) -> str:
    extension = file.suffix.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Other"
