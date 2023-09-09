from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    browser.find_element(By.ID,'book').click()


    browser.find_element(By.XPATH,'/html/body/form/div/div/button').click()
    x = browser.find_element(By.XPATH,'//*[@id="input_value"]')
    x = calc(x.text)
    browser.find_element(By.ID,'answer').send_keys(x)
    browser.find_element(By.XPATH,'/html/body/form/div/div/button').click()

finally:
    time.sleep(5)
    browser.quit()