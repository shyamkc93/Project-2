import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Test Case ID:TC-Login_01(Valid user name and Valid password)

driver = webdriver.Firefox(executable_path="c:\webdrivers\geckodriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_xpath("//input[@class='oxd-input oxd-input--active']").send_keys("Admin")
driver.find_element_by_xpath("//input[@class='oxd-input oxd-input--active']").send_keys("admin123")
driver.find_element_by_xpath("//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
time.sleep(4)
driver.implicitly_wait(20)
logout = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span'
logout1 = '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
driver.find_element(By.XPATH, logout).click()
driver.find_element(By.XPATH,logout1).send_keys(Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.ENTER)

#Test Case ID:TC-Login_02(Valid user name and In-Valid password)

driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin345")
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
