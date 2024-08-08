from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

from config.config import ConfigFile

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

    driver.get("http://automated.pythonanywhere.com/login/")

    return driver


def split_text(text):
    output = text.split(": ")[1]   #float(text.split(":")[2])
    return output


def write_file(text):
    filename = "seconds_file.txt"
    with open(filename,'a') as file:
        file.write(f"{text} ")


def main():
    driver = get_driver()
    config = ConfigFile.get_config()
    user = config['automated_user']
    password = config['automated_pass']
    driver.find_element(by="id",value="id_username").send_keys(user)
    time.sleep(2)
    driver.find_element(by="id",value="id_password").send_keys(password + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    element = driver.find_element(by="xpath",value="/html/body/nav/div/div/div[2]/div")
    print(colored(f"username : {element.text}","red"))
    
    t_end = time.time() + 30
    while time.time() <= t_end:
        time.sleep(2)
        scraped_time = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
        seconds = split_text(scraped_time.text)
        write_file(seconds)
        print(colored(f"{seconds}","blue"))
        

print(colored(f"here is the scrapped txt : {main()}","red"))