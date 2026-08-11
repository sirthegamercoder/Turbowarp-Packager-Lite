import sys
import os
from pathlib import Path
from PyInstaller.__main__ import run

script_dir = Path(__file__).parent.absolute()
os.chdir(script_dir)

name_game_path = script_dir / "assets" / "name-project.txt"
with open(name_game_path, 'r') as file:
    name_game = file.read()

default_exclude_modules = [
    'tkinter',
    'gevent',
    'greenlet',
    'markupsafe',
    'psutil',
    'setuptools',
    'shiboken6',
    'tcl8',
    'tomli',
    'zope.event',
    'zope.interface',
    'PySide6'
]

exclude_choice = input("Do you want to exclude modules? (Y/n): ").strip().lower()

exclude_modules = []
if exclude_choice in ['', 'y', 'yes']:
    user_input = input(f"Enter module names to exclude (comma-separated, press Enter for default): ").strip()
    
    if user_input:
        exclude_modules = [m.strip() for m in user_input.split(',') if m.strip()]
    else:
        exclude_modules = default_exclude_modules
        print(f"Using default exclusions: {', '.join(default_exclude_modules)}")
else:
    print("Skipping module exclusions")

base_args = [
    '--noconfirm',
    '--onedir',
    '--windowed',
    f'--distpath={script_dir / "export" / "dist"}',
    f'--workpath={script_dir / "export" / "build"}',
    f'--specpath={script_dir / "export"}',
    f'--name={name_game}',
    '--clean',
]

if sys.platform == "win32":
    base_args.append(f'--icon={script_dir / "assets" / "icon.ico"}')
elif sys.platform == "darwin":
    base_args.append(f'--icon={script_dir / "assets" / "icon.icns"}')
else:
    pass

if sys.platform == "win32":
    base_args.append(f'--add-data={script_dir / "assets"};assets/')
else:
    base_args.append(f'--add-data={script_dir / "assets"}:assets/')

for module in exclude_modules:
    base_args.append(f'--exclude-module={module}')

base_args.append(str(script_dir / "app" / "window.py"))

if __name__ == "__main__":
    print(f"Building {name_game}...")
    print(f"Excluding modules: {', '.join(exclude_modules) if exclude_modules else 'None'}")
    run(base_args)