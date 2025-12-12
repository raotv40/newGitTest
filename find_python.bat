@echo off
echo Searching for Python installations...
echo.

echo === Checking common Python locations ===
if exist "C:\Python27" echo Found: C:\Python27
if exist "C:\Python36" echo Found: C:\Python36
if exist "C:\Python37" echo Found: C:\Python37
if exist "C:\Python38" echo Found: C:\Python38
if exist "C:\Python39" echo Found: C:\Python39
if exist "C:\Python310" echo Found: C:\Python310
if exist "C:\Python311" echo Found: C:\Python311
if exist "C:\Python312" echo Found: C:\Python312
if exist "C:\Python313" echo Found: C:\Python313

echo.
echo === Checking User AppData ===
if exist "%LOCALAPPDATA%\Programs\Python" (
    echo Found Python folder in: %LOCALAPPDATA%\Programs\Python
    dir /b "%LOCALAPPDATA%\Programs\Python"
)

echo.
echo === Checking Program Files ===
if exist "C:\Program Files\Python" (
    echo Found: C:\Program Files\Python
    dir /b "C:\Program Files\Python"
)
if exist "C:\Program Files (x86)\Python" (
    echo Found: C:\Program Files (x86)\Python
    dir /b "C:\Program Files (x86)\Python"
)

echo.
echo === Checking PATH environment variable ===
where python 2>nul
if %errorlevel% equ 0 (
    echo Python found in PATH
) else (
    echo Python NOT found in PATH
)

echo.
echo === Checking for py launcher ===
where py 2>nul
if %errorlevel% equ 0 (
    echo Python Launcher found. Running: py --version
    py --version
    echo Python Launcher location:
    py -0p
)

pause
