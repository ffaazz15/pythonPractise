import time


import driver as driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By





driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# driver.implicitly_wait(2)
driver.maximize_window()
driver.get('https://www.flipkart.com/')


driver.find_element(By.XPATH("/html/body/div[3]/div/div/button")).click()

time.sleep(13)

