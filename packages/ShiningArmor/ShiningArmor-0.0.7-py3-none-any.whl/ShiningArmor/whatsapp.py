from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from time import time, ctime, sleep


def wa_init():
    # Initialize WhatsApp
    rc = 0
    t = time()

    try:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("user-data-dir=" + "cookies")

        display = Display(visible=0)
        display.start()

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get('https://web.whatsapp.com')

        sleep(20)
    except Exception as err:
        print(f'{ctime(t)} | Exception occurred in wa_init() function \n {err}')
        rc = 1

    return rc, driver, display


def wa_close(driver, display):
    # close connection to WhatsApp
    driver.quit()
    display.stop()


def wa_locate_contact(driver, wa_contact):
    # Find the WhatsApp contact
    rc = 0
    t = time()

    try:
        driver.find_element_by_xpath('//*[@title = "{}"]'.format(wa_contact)).click()
        sleep(10)
    except Exception as err:
        print(f'{ctime(t)} | Exception occurred in wa_contact() function \n {err}')
        rc = 1

    return rc


def wa_send_message(driver, display, wa_message_list):
    rc = 0
    t = time()

    try:
        wa_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]')

        # message in one-block
        for i in wa_message_list:
            wa_msg.send_keys(i + Keys.SHIFT + Keys.RETURN)

        wa_msg.send_keys(Keys.ENTER)
        sleep(15)

        print(f'{ctime(t)} | WhatsApp message successfully sent!')

        wa_close(driver, display)

    except Exception as err:
        print(f'{ctime(t)} | Exception occurred in wa_contact() function \n {err}')
        rc = 1

    return rc