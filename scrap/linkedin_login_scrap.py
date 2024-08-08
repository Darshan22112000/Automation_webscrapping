from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
from io import StringIO
from csv import reader
from webdriver_manager.chrome import ChromeDriverManager

from config.config import ConfigFile


# service = Service("C:\chromedriver-win64\chromedriver.exe")

def get_driver():

    options = webdriver.ChromeOptions()

    options.add_argument("disable-infobar")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-feature=AutomationControlled")

    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.linkedin.com/login?trk=homepage-basic_intl-segments-login")

    return driver


def split_text(text):
    output = text.split(":")[2]   #float(text.split(":")[2])
    return output

#filename = "california_linkedin_search_result.txt"
#with open(filename, 'a', encoding="utf-8") as file:
#file.write(f"\n{project}\n")
def write_to_file(project, job_role, location):
    cwd = os.getcwd()
    filename = f"{job_role}_{location}_linkedin"
    upload_file_path = os.path.join(cwd, f'{filename}.xlsx').replace("\\", '/')
    # upload_file_path = r'C:\Users\Darshan Vetal\Desktop\Learning\python\python automation\project\scrap\{}.xlsx'.format(filename)
    # filename_split = filename.split('.')
    project.to_excel(upload_file_path, encoding='utf-8', index=False)

def main():
    driver = get_driver()
    config = ConfigFile.get_config()
    user = config['github_user']
    password = config['github_pass']
    driver.find_element(by="id", value="username").send_keys(user)
    time.sleep(2)
    driver.find_element(by="id", value="password").send_keys(password + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="//*[@id='global-nav']/div/nav/ul/li[3]/a").click()
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]").click()
    time.sleep(2)

    job_role = 'Data Analyst'
    location = 'Dublin'
    no_of_records = 100

    driver.find_element(by="xpath", value="/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]").send_keys(job_role)
    time.sleep(2)
    driver.find_element(by="xpath",
                        value="/html/body/div[6]/header/div/div/div/div[2]/div[3]/div/div/input[1]").send_keys(location + Keys.ENTER)
    time.sleep(2)
    print(colored(driver.current_url, "red"))

    project2 = pd.DataFrame()
    li_list = []
    for i in range(1, no_of_records):
        try:
            project = driver.find_element(by="xpath", value=f"//*[@id='main']/div/div[2]/div[1]/div/ul/li[{i}]")
            li_list.append(project.text)
            #project = StringIO(project)
            #project = pd.read_csv(project, sep="\n")
            #project1 = pd.DataFrame(project)
            # project2 = project2.append(project1)
        except:
            pass

    project2 = pd.DataFrame(li_list, columns=['List Data'])
    write_to_file(project2, job_role, location)

print(colored(f"\nhere is the scrapped txt : {main()}", "red"))