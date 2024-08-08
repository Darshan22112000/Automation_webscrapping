from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from config.config import ConfigFile

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

    driver.get("https://github.com/login")

    return driver


def split_text(text):
    output = text.split(":")[2]   #float(text.split(":")[2])
    return output

def write_to_file(project):
    filename = "github_search_result.txt"
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(f"\n{project}\n")

def main():
    driver = get_driver()
    config = ConfigFile.get_config()
    user = config['github_user']
    password = config['github_pass']
    driver.find_element(by="id", value="login_field").send_keys(user)
    time.sleep(2)
    driver.find_element(by="id", value="password").send_keys(password + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/div[1]/header/div[3]/div/div/form/label/input[1]").send_keys("web scrapping" + Keys.RETURN)
    print(colored(driver.current_url, "red"))
    
    for i in range(1, 11):
        time.sleep(2)
        project = driver.find_element(by="xpath", value=f"/html/body/div[5]/main/div/div[3]/div/ul/li[{i}]").text
        write_to_file(project)
    
    
print(colored(f"here is the scrapped txt : {main()}", "red"))