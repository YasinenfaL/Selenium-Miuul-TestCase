##############################################
# Selenium Study
##############################################

# Libraries
import os
import sys
import requests
import time
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--no-sandbox");
options.add_argument("enable-automation");
options.add_argument("disable-infobars");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--disable-browser-side-navigation");
options.add_argument("--disable-gpu");
options.add_argument("window-size=1900,1000")


##############################################
# Study Solution
##############################################

def fill_form_miuul(name, surname, email, phone_number, program_name, message):
    """
    Fills a form with the specified name, surname, e-mail, phone number, program name and message information.
    Args:
        name (str): First Name of applicant.
        surname (str): Last name of the applicant.
        email (str): Email address of the applicant
        phone_number (str): Phone number of the applicant.
        program_name (str): The name of the referenced program.
        message (str): The message that the applicant wants to add.

    Returns:
        str: Operation result message.

    """
    url = "https://www.miuul.com/data-scientist-bootcamp"
    driver = webdriver.Chrome(executable_path="C:/Users/Yasin/selenium/chromedriver.exe", options=options)
    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 60)

    apply = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[3]/main/section[1]/div/div[2]/div/div/a")))
    apply.click()

    name_input = WebDriverWait(driver, 10). \
        until(EC.presence_of_element_located((By.ID, "exampleFormControlInput1")))
    name_input.send_keys(name, Keys.TAB)

    driver.execute_script("arguments[0].scrollIntoView();", name_input)
    time.sleep(5)

    current_input = driver.switch_to.active_element
    time.sleep(5)

    current_input.send_keys(surname, Keys.TAB)
    current_input1 = driver.switch_to.active_element
    time.sleep(3)

    current_input1.send_keys(email, Keys.TAB)
    time.sleep(3)

    current_input2 = driver.switch_to.active_element
    time.sleep(3)

    current_input2.send_keys(phone_number, Keys.TAB)
    time.sleep(3)

    current_input3 = driver.switch_to.active_element
    time.sleep(3)

    current_input3.send_keys(program_name, Keys.TAB)
    time.sleep(3)

    current_input4 = driver.switch_to.active_element
    time.sleep(3)

    current_input4.send_keys(message, Keys.TAB)
    time.sleep(3)

    driver.quit()
    return "The form has been successfully filled."


fill_form_miuul("Yasin", "Üzümcü", "enfalu@gmail", "5355252211", "Veri Bilimi Kayıt", "Boot camp'de görüşmek üzere")
