## import dependencies
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd

# Puts series of singnup requests to the jupyterhub server with open
# registration. Useful to create user accounts with predefined
# passwords. The passwords have to be distributed by a secret method
# to the users.

df = pd.read_csv('hesla_kombi.csv')
df = pd.read_csv('hesla_pres.csv')
df['heslo'] = '2024_'+df['heslo']

server = "https://jupyter.mendelu.cz"

## create an object of the chrome webdriver
driver = webdriver.Chrome(executable_path = r'./chromedriver')

## open selenium URL in chrome browser
driver.get(server+'/hub/signup')
driver.get(server+'/hub/login')

login, heslo = "admin","klokan524524"
inputElement = driver.find_element("id","username_input")
inputElement.send_keys(login)
inputElement = driver.find_element("id","password_input")
inputElement.send_keys(heslo)
time.sleep(1) # Let the user actually see something!
inputElement.submit()
time.sleep(8) # Let the user actually see something!


for i,(jmeno,login, heslo) in df.iterrows():
    print (r"\prikaz ",login,";",jmeno,";",heslo,";")
    
    
    driver.get(server+'/hub/change-password/'+login)
    inputElement = driver.find_element("id","new_password_input")
    inputElement.send_keys(heslo)
    inputElement = driver.find_element("id","new_password_confirmation_input")
    inputElement.send_keys(heslo)



    # inputElement = driver.find_element("id","username_input")
    # inputElement.send_keys(login)
    # inputElement = driver.find_element("id","password_input")
    # inputElement.send_keys(heslo)
    # inputElement = driver.find_element("id","password_confirmation_input")
    # inputElement.send_keys(heslo)

    time.sleep(1) # Let the user actually see something!
    inputElement.submit()
    time.sleep(1) # Let the user actually see something!


driver.quit()
