@echo off

set "PROJECT_ROOT=%~dp0"
set "PYTHON=%PROJECT_ROOT%backend\.venv\Scripts\python.exe"
set "SCRIPT=%PROJECT_ROOT%backend\main.py"

if not exist "%PYTHON%" (
    echo Error: Python virtual environment was not found.
    echo Expected: %PYTHON%
    pause
    exit /b 1
)

echo Running Download Organiser...
echo.

"%PYTHON%" "%SCRIPT%"

echo.
if errorlevel 1 (
    echo The organiser encountered an error.
) else (
    echo Finished successfully.
)

pause