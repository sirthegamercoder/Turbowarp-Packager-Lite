import os
import sys
import webview

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    html_file = resource_path("assets/index.html")
    da_name_game = resource_path("assets/name-project.txt")
    icon_app_game = resource_path("assets/icon.ico") if sys.platform == "win32" else resource_path("assets/icon.png")

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

if __name__ == "__main__":
    main()