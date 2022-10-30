import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Test Case ID:TC-PIM_01


driver = webdriver.Firefox(executable_path="c:\webdrivers\geckodriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_xpath("//input[@class='oxd-input oxd-input--active']").send_keys("Admin")
driver.find_element_by_xpath("//input[@class='oxd-input oxd-input--active']").send_keys("admin123")
driver.find_element_by_xpath("//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()

PIM = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
PIM.click()
Add = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
Add.click()
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Shyam")
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys("Sundar")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys("M")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
driver.find_element_by_xpath("//span [@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
driver.implicitly_wait(20)

driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys("Shyam@kc017")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys("Shyam@123")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys("Shyam@123")
Save = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
Save.click()


#Test Case ID:TC-PIM_02


driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input').send_keys("Shyam")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys("TN77Z20200000622")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys("2033-06-11")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]').send_keys("Indian")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]').send_keys("Single")
driver.find_element_by_xpath('//html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').send_keys("1993-06-12")
driver.find_element_by_xpath("//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']").click()
driver.implicitly_wait(20)
Save = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')
Save.click()
#driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]").send_keys("B+")
driver.implicitly_wait(20)
Save = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')
Save.click()

driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Phoneix Mall Velacheri")
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Nehru nagar")
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").send_keys("Chennai")
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Tamil Nadu")
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input").send_keys("600042")
driver.implicitly_wait(20)
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]").send_keys("India")
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input").send_keys("9943514222")
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("7695963271")
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input").send_keys("1")
#driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input").send_keys("shyamm93sundar42@gmail.com")
#driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input").send_keys("shyam422sundar19@gmail.com")
driver.implicitly_wait(20)
Save = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')
Save.click()

driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("2019-06-12")
driver.implicitly_wait(20)
"""Engineer = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]'
driver.find_element(By.XPATH,Engineer).click()
driver.find_element(By.XPATH,Engineer).send_keys(Keys.DOWN,Keys.DOWN,Keys.ENTER)
Office = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div'
driver.find_element(By.XPATH,Office).click()
driver.find_element(By.XPATH,Office).send_keys(Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.ENTER)
driver.implicitly_wait(20)
Freelance = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]'
driver.find_element(By.XPATH,Freelance).click()
driver.find_element(By.XPATH,Freelance).send_keys(Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.ENTER)"""

Save = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button')
Save.click()


#Test Case ID:TC-PIM_03


driver.implicitly_wait(20)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Shyam Sundar M")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys("0288")
driver.implicitly_wait(20)
Search = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
Search.click()
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i').click()

