from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

path = os.path.abspath(os.getcwd())
driver = webdriver.Chrome('{}\\chromedriver.exe'.format(path))
driver.get("https://popcat.click/")
element = driver.find_element(By.TAG_NAME, 'div')
x = 0
while(x < 10000):
    element.click()
    x = x + 1
