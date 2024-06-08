# Grab Discord Token with QR

Grab Discord login tokens easily by scamming the victim with a fake QR code than will make you login instead of giving the victim free nitro.

### About

A Python script that automatically generates a Nitro scam QR code and grabs the Discord token when scanned. This tool demonstrates how people can trick others
into scanning their Discord login QR Code, and gain access to their account. Use for Educational Purposes only.

![img1](https://cdn.discordapp.com/attachments/853817893744803840/899317048977551410/unknown.png)

## Initial Setup

Download the correct version of [chromedriver](https://chromedriver.chromium.org/downloads), and paste the `chromedriver.exe` to the current path

### Troubleshooting

Make sure your `chromedriver.exe` file is the same version as your current Chrome web browser version. To check your current Chrome version,
paste `chrome://settings/help` in Google Chrome.

if Chrome crashes,

1. Make sure your chromedriver.exe file is the same version as your Chrome web browser version
2. Download the latest version chromedriver.exe here: [Click Here](https://chromedriver.chromium.org/downloads)

3. Then replace the chromedriver.exe file in the folder.

OR

3. copy the `cromedriver.exe` to the system32 folder

## Usage

### Setup

1. If you dont have python installed, download python 3
   and make sure you click on the 'ADD TO PATH' option during
   the installation.

2. Open cmd in the current folder and run `py -m pip install -r requirements.txt`

3. Run `py token-grabber.py` in cmd to run the program

4. Wait for the `discord_gift.png` to be generated in the current working directory. Send the image to the victim and make them scan it.

5. QR Code only lasts about 2 minutes. Make sure you send a fresh one to the victim and he is ready to scan.

6. When the QR Code is scanned, you will automatically be logged in to their account and the script will grab the Discord token.


### Advanced Usage

#### Help

```
> python .\token-grabber.py --help
usage: start.py [-h] [--verbose] [--logs] [--save [SAVE]] [--time TIME]

A script to grab data with various options.

options:
  -h, --help     show this help message and exit
  --verbose      Enable verbose output
  --logs         Enable logging
  --save [SAVE]  Specify the filename to save the data (default is tokens.txt)
  --time TIME    Set the time (default is 4)
```

#### Advanced Examples

```bash
python token-grabber.py                      # default use
python token-grabber.py --help               # display help message
python token-grabber.py --verbose            # log everything, verbosely
python token-grabber.py --logs               # save logs to file
python token-grabber.py --save tokens.txt    # save results to `tokens.txt`
python token-grabber.py --time 5             # set waiting time to 5 seconds
```

- Note: the waiting time should be increased if you have a slow internet connection. This defaults to 4 seconds and it works fine with a 2Mbps internet connection.


#### Note: This is illegal and i am not responsible for anything done with this tool. I maintain this tool only for educational purposes
