from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, time
import random
import string


driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())

''' Website Link:- https://console.uat.asians.group/#/domain/list
This is UI test automation for Registration functionality using the website link'''

driver.get("https://console.uat.asians.group/#/domain/list")
driver.maximize_window()  #Here the window will be Maxamized
sleep(4)
driver.find_element(By.XPATH, '//*[@id="kc-registration"]/span/a').click() # After Opening The Website Link this X path will redirected to the registartion button and click that
email = driver.find_element(By.ID, "email")
sleep(4)
emailID = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) # Here I have taken the some random email id so would be easy to test.
email.send_keys(emailID+"@gmail.com")
sleep(4)
pswd = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) #Here I have taken the some random Password so would be easy to test.
driver.find_element(By.ID, "password").send_keys(pswd)
driver.find_element(By.ID, "password-confirm").send_keys(pswd) #Here I have taken the some random Password and it also confirm the same so would be easy to test
sleep(5)
driver.find_element(By.XPATH, '//*[@id="kc-form-buttons"]/input').click() # here it click to submit button and it open the page.
sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div/header/ul[3]/li/a/div/span').click() # here it click to profile button
sleep(4)
driver.find_element(By.XPATH, '/html/body/div[1]/div/header/ul[3]/li/div/a[4]/button').click() #in the Xpath the profile will be Logout.
sleep(4)
driver.switch_to.new_window('none') # After making the New Registration Account the window will open a new tab so It can go to the log in page.
sleep(4)


''' Website Link:- https://console.uat.asians.group/#/domain/list
This is UI test automation for Login functionality using the website link'''

driver.get("https://user.asians.group/auth/realms/asians/protocol/openid-connect/auth?client_id=public&redirect_uri=https%3A%2F%2Fconsole.uat.asians.group%2F%23%2Fdomain%2Flist&state=4d773edc-2e3d-4146-b697-305a7a20e44f&response_mode=fragment&response_type=code&scope=openid&nonce=f9316d18-039d-4e93-8091-10240c18f2f0")
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(emailID+"@gmail.com") # In the login page it take the same email id which we have entered during the Registration.
sleep(4)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(pswd) # In the login page it take the same Password which we have entered during the Registration.
sleep(3)
driver.find_element(By.XPATH, '//*[@id="rememberMe"]').click() # here it confirm the checkbox
sleep(3)
driver.find_element(By.XPATH, '//*[@id="kc-login"]').click() # here it confirm the login button.
sleep(5)
print(driver.title)
driver.close()