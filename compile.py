import sys
import os
from pathlib import Path
from PyInstaller.__main__ import run

script_dir = Path(__file__).parent.absolute()
os.chdir(script_dir)

name_game_path = script_dir / "assets" / "name-project.txt"
with open(name_game_path, 'r') as file:
    name_game = file.read()

if sys.platform == "win32":
    args = [
        '--noconfirm',
        '--onedir',
        '--windowed',
        f'--distpath={script_dir / "export" / "dist"}',
        f'--workpath={script_dir / "export" / "build"}',
        f'--specpath={script_dir / "export"}',
        f'--icon={script_dir / "assets" / "icon.ico"}',
        f'--name={name_game}',
        '--clean',
        f'--add-data={script_dir / "assets"};assets/',
        '--exclude-module=tkinter',
        '--exclude-module=gevent',
        '--exclude-module=greenlet',
        '--exclude-module=markupsafe',
        '--exclude-module=psutil',
        '--exclude-module=setuptools',
        '--exclude-module=shiboken6',
        '--exclude-module=tcl8',
        '--exclude-module=tomli',
        '--exclude-module=zope.event',
        '--exclude-module=zope.interface',
        '--exclude-module=PySide6',
        str(script_dir / "app" / "window.py")
    ]
else:
    args = [
        '--noconfirm',
        '--onedir',
        '--windowed',
        f'--distpath={script_dir / "export" / "dist"}',
        f'--workpath={script_dir / "export" / "build"}',
        f'--specpath={script_dir / "export"}',
        f'--name={name_game}',
        '--clean',
        f'--add-data={script_dir / "assets"}:assets/',
        '--exclude-module=tkinter',
        '--exclude-module=gevent',
        '--exclude-module=greenlet',
        '--exclude-module=markupsafe',
        '--exclude-module=psutil',
        '--exclude-module=setuptools',
        '--exclude-module=shiboken6',
        '--exclude-module=tcl8',
        '--exclude-module=tomli',
        '--exclude-module=zope.event',
        '--exclude-module=zope.interface',
        '--exclude-module=PySide6',
        str(script_dir / "app" / "window.py")
    ]

if __name__ == "__main__":
    run(args)