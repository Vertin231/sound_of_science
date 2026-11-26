@echo off
setlocal
chcp 65001 >nul
title Sound of Science - Classroom Launcher

REM Always run from the USB/project folder, regardless of the current directory.
cd /d "%~dp0"

echo.
echo ==========================================
echo       SOUND OF SCIENCE - CLASSROOM
echo ==========================================
echo.

set "PYTHON_CMD="
set "PYTHON_ARGS="

REM Prefer the Windows Python Launcher.
where py >nul 2>nul
if not errorlevel 1 (
    py -3 -c "import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>nul
    if not errorlevel 1 (
        set "PYTHON_CMD=py"
        set "PYTHON_ARGS=-3"
    )
)

REM Fall back to python on PATH.
if not defined PYTHON_CMD (
    where python >nul 2>nul
    if not errorlevel 1 (
        python -c "import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>nul
        if not errorlevel 1 (
            set "PYTHON_CMD=python"
        )
    )
)

if not defined PYTHON_CMD (
    echo [ERROR] Python 3.10 or newer was not found.
    echo Install Python 3.11 or newer from https://www.python.org/downloads/
    echo During installation, enable "Add Python to PATH".
    echo Then run this file again.
    pause
    exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
    echo [1/4] Creating a project-local virtual environment...
    %PYTHON_CMD% %PYTHON_ARGS% -m venv .venv
    if errorlevel 1 goto :error
)

set "VENV_PY=%~dp0.venv\Scripts\python.exe"

echo [2/4] Updating pip...
"%VENV_PY%" -m pip install --upgrade pip
if errorlevel 1 goto :error

echo.
echo [3/4] Checking/installing project dependencies.
echo This may take several minutes the first time. Internet access is required.
"%VENV_PY%" -m pip install -r requirements.txt
if errorlevel 1 goto :error

echo.
echo [4/4] Starting JupyterLab...
echo Keep this window open during the presentation.
echo To stop the server, close this window or press Ctrl+C.
echo.
"%VENV_PY%" -m jupyter lab main.ipynb
if errorlevel 1 goto :error
exit /b 0

:error
echo.
echo [ERROR] Setup or startup failed.
echo Check the messages above. Make sure this computer has internet access.
pause
exit /b 1
