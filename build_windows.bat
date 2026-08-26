@echo off
setlocal
python -m pip install -r requirements.txt
python -m pip install pyinstaller
pyinstaller --noconfirm --clean --onefile --windowed --name ExcelAutomationTool main.py
 echo.
echo Build finished. The executable is in the dist folder.
pause
