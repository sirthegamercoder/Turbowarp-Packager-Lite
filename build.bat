@echo off
cd /d "%~dp0"
set /p NameGame=<"assets/name-project.txt"

pyinstaller --noconfirm --onedir --windowed --icon "%~dp0\assets\icon.ico" --name "%NameGame%" --clean --add-data "%~dp0\assets;assets/" --exclude-module=tkinter --exclude-module=gevent --exclude-module=greenlet --exclude-module=markupsafe --exclude-module=psutil --exclude-module=markupsafe --exclude-module=setuptools --exclude-module=shiboken6 --exclude-module=tcl8 --exclude-module=tomli --exclude-module=zope.event --exclude-module=zope.interface --exclude-module=PySide6 "app\window.py"

pause
exit