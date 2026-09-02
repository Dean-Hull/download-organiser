# Download Organiser

A Python utility that organises files in the Windows Downloads folder by file type and modification year.

## Folder structure

```text
Downloads/
├── Documents/
│   ├── 2025/
│   └── 2026/
├── Images/
├── Videos/
├── Audio/
├── Archives/
├── Installers/
└── Other/
```

## How it works

The program:

1. Scans top level files in the Downloads folder.
2. Categorises each file by its extension.
3. Reads the file's last modified year.
4. Creates category and year folders.
5. Moves each file into the appropriate folder.

Existing folders are ignored. If the destination already contains a file with the same name, the source file is skipped.

## Requirements

- Windows
- Python 3

No external Python packages are required.

## Setup

Clone the repository:

```powershell
git clone https://github.com/Dean-Hull/download-organiser.git
cd download-organiser
```

Create the virtual environment used by `run.bat`:

```powershell
cd backend
py -m venv .venv
cd ..
```

## Run

Double-click `run.bat` or run it from PowerShell:

```powershell
.\run.bat
```

## Preview changes

Open `backend/main.py` and set:

```python
organise_files(files, downloads, dry_run=True)
```

This displays the proposed destinations without moving files.

To move the files, set:

```python
organise_files(files, downloads, dry_run=False)
```

## Customise categories

File categories and extensions are defined in:

```text
backend/file_categories.py
```

Add or remove entries from `FILE_TYPES`:

```python
FILE_TYPES = {
    "Documents": {
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
    },
    "Images": {
        ".jpg",
        ".jpeg",
        ".png",
    },
}
```

Files with extensions that are not listed are placed in the `Other` folder.

## Project structure

```text
download-organiser/
├── backend/
│   ├── file_categories.py
│   ├── main.py
│   ├── scan.py
│   └── utils.py
├── run.bat
├── .gitignore
└── README.md
```

## Notes

- Only top-level files in Downloads are organised.
- Existing folders are not modified.
- Files are grouped by their last modified year.
- Duplicate destination filenames are skipped.
- The batch file is intended for Windows.