## import dependencies
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd

# Puts series of singnup requests to the jupyterhub server with open
# registration. Useful to create user accounts with predefined
# passwords. The passwords have to be distributed by a secret method
# to the users.

server = "https://jupyter.mendelu.cz"

logins_passwords = [[i[1][0],i[1][1]] for i in pd.read_csv("hesla.csv", header=None).iterrows()]

## create an object of the chrome webdriver
driver = webdriver.Chrome(executable_path = r'./chromedriver')

## open selenium URL in chrome browser
driver.get(server+'/hub/signup')

for login, heslo in logins_passwords:
    inputElement = driver.find_element("id","username_input")
    inputElement.send_keys(login)
    inputElement = driver.find_element("id","password_input")
    inputElement.send_keys(heslo)
    inputElement = driver.find_element("id","password_confirmation_input")
    inputElement.send_keys(heslo)
    time.sleep(3) # Let the user actually see something!
    inputElement.submit()
    time.sleep(3) # Let the user actually see something!


driver.quit()
