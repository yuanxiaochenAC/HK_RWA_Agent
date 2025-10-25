@echo off
REM RWA Intelligent Consultation System - Windows Batch Launcher
REM Automatically sets UTF-8 encoding to fix Unicode character display issues

echo ================================================================================
echo                    RWA INTELLIGENT CONSULTATION SYSTEM
echo                     Windows UTF-8 Encoding Auto-Setup
echo ================================================================================
echo.

REM Switch to UTF-8 code page
chcp 65001 >nul 2>&1

REM Set Python encoding environment variable
set PYTHONIOENCODING=utf-8

REM Activate virtual environment if it exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo Warning: Virtual environment not found. Using system Python.
)

echo.
echo System ready. Starting RWA Consultation System...
echo.

REM Run the Python script with all passed arguments
python run_rwa_consultant.py %*

REM Keep window open if there was an error
if errorlevel 1 (
    echo.
    echo Error occurred. Press any key to close...
    pause >nul
)
