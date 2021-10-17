import os
import platform
import json


class OSdiff:
    if platform.system().lower().startswith('win'):
        pip = "pip3"
        python = "python"
        clear = "cls"
        windows = True
    else:
        pip = "pip3"
        python = "python3"
        clear = "clear"
        linux = True


class Config:
    with open("dtg/config.json", "r", encoding="utf-8") as conf:
        data = json.loads(conf.read())

    try:
        CLI_SLEEP_TIME = int(data["CLI_SLEEP_TIME"])
    except:
        print("- Please enter a valid value for CLI_SLEEP_TIME in dtg/config.json")


def clear_screen():
    if platform.system().lower().startswith('win'):
        os.system("cls")
    else:
        os.system("clear")


def show_logo():
    print("""
        ____ _____ ____ 
        |  _ \_   _/ ___|
        | | | || || |  _ 
        | |_| || || |_| |
        |____/ |_| \____|
     Discord Token Generator
         """)


def create_requirements_file():
    with open("requirements.txt", "w") as req_file:
        req_file.write("""beautifulsoup4
selenium
pillow
lxml""")


def install_requirements_file():
    os.system(f"{OSdiff.pip} install -r requirements.txt")


def remove_requirements_file():
    try:
        os.remove("requirements.txt")
    except:
        if OSdiff.windows:
            os.system("rem /q requirements.txt")
        if OSdiff.linux:
            os.systen("rm -rf requirements.txt")
