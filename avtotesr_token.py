import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://127.0.0.1:8000/api/v1/token/"

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser




class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        print('test1')
        browser.get(link)
        time.sleep(10)
        input1 = browser.find_element(By.XPATH, '//div//input[@type="text"]')
        input1.send_keys('Daria')
        input2 = browser.find_element(By.XPATH, '//div//input[@type="password"]')
        input2.send_keys('10121991')
        time.sleep(5)
        input3 = browser.find_element(By.XPATH, '//div//button[text()="POST"]')
        input3.click()
        time.sleep(5)


