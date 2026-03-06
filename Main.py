from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.drfrostmaths.com/timestables-game.php")
inputElement = driver.find_element(By.XPATH,'//*[@id="dfm-home-inner-content"]/input[1]')
sleep(2)
inputElement.send_keys('username')  # change username
inputElement = driver.find_element(By.XPATH,'//*[@id="dfm-home-inner-content"]/input[2]')
inputElement.send_keys('password') # change password

inputElement = driver.find_element(By.XPATH,'//*[@id="login-submit-button"]').click()
sleep(1)
inputElement = driver.find_element(By.XPATH,'//*[@id="question"]/a').click()
sleep(0.1)
for i in range(61):
    inputElement = driver.find_element(By.ID,'question')
    a = eval(inputElement.text.replace('×','*').replace('÷','/'))

    inputElement = driver.find_element(By.XPATH,'//*[@id="calculator-display"]')
    inputElement.send_keys(int(a))

                    
