from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\chromedriver-win64\chromedriver.exe")

def get_driver():

    options = webdriver.ChromeOptions()

    options.add_argument("disable-infobar")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-feature=AutomationControlled")

    driver = webdriver.Chrome(service=service,options=options)

    driver.get("http://automated.pythonanywhere.com/login/")

    return driver


def split_text(text):
    output = text.split(":")[2]   #float(text.split(":")[2])
    return output


def main():
    driver = get_driver()
    
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    element = driver.find_element(by="xpath", value="/html/body/nav/div/div/div[2]/div")
    return element.text
    

print(colored(f"here is the scrapped txt : {main()}", "red"))