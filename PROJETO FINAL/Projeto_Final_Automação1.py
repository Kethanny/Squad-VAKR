from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = Firefox()

link = 'https://projetofinal.jogajuntoinstituto.org/'
browser.get(link)

input_email = browser.find_element(By.NAME, "email")
input_email.send_keys('kethynayane816@gmail.com')

input_senha = browser.find_element(By.NAME, "password")
input_senha.send_keys('kethy123')
input_senha.send_keys(Keys.ENTER)

time.sleep(10) 

result_search = browser.find_elements(By.TAG_NAME, 'h3')

check = False

for result in result_search:
    if 'Instituto Joga Junto' in result.text:
        result.click()
        print("Link encontrado e clicado!")
        check = True
        break



browser.quit()
