import os
import sys
import webview
import subprocess

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def preview_game():
    html_file = resource_path("assets/index.html")
    da_name_game = resource_path("assets/name-project.txt")
    icon_app_game = resource_path("assets/icon.ico") if sys.platform == "win32" elif sys.platform == "darwin" resource_path("assets/icon.icns") else resource_path("assets/icon.png")

    with open(da_name_game, "r", encoding="utf-8") as file:
        name_game = file.read()

    width, height = 480, 360

    try:
        screen = webview.screens[0]
        x = (screen.width - width) // 2
        y = (screen.height - height) // 2
    except Exception:
        x, y = None, None

    window = webview.create_window(name_game, html_file, width=width, height=height, x=x, y=y)
    webview.start(http_server=True, icon=icon_app_game)

def main():
    da_file = resource_path("assets/name-project.txt")

    with open(da_file, "w"):
        pass

    user_input = input("Enter Scratch/Turbowarp project name: ")
    if not user_input:
        print("Project name cannot be empty!")
        sys.exit(1)

    convert = input("Convert to lowercase and hyphenated? (y/n): ").lower()
    
    if convert == "y" or convert == "yes":
        proceed_input = user_input.lower().replace(" ", "-")
        print(f"Converted to: {proceed_input}")
    else:
        proceed_input = user_input
        print(f"Keeping original: {proceed_input}")

    with open(da_file, "w", encoding="utf-8") as file:
        file.write(proceed_input)

    choice = input("Type \"test\" to preview or \"compile\" to convert to EXE: ")

    if choice == "test":
        preview_game()
    elif choice == "compile":
        subprocess.run([sys.executable, "compile.py"])
    else:
        print("Invalid user's input.")

if __name__ == "__main__":
    main()