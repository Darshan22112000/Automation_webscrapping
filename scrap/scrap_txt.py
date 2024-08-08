from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:\chromedriver_win32\chromedriver.exe")

def get_driver():

    options = webdriver.ChromeOptions()

    options.add_argument("disable-infobar")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-feature=AutomationControlled")

    driver = webdriver.Chrome(service=service,options=options)

    driver.get("https://time.is/")

    return driver


def split_text(text):
    output = text.split(":")[2]   #float(text.split(":")[2])
    return output


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[2]/div[2]/div[2]/div/time")
    return element.text
    #return split_text(element.text)

print(colored(f"here is the scrapped txt : {main()}","red"))