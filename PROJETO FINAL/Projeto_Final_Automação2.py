from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa o WebDriver do Firefox
browser = Firefox()


# Acesse o link
link = 'https://projetofinal.jogajuntoinstituto.org/'
browser.get(link)

# Encontre o campo de e-mail e envie o e-mail
input_email = browser.find_element(By.NAME, "email")
input_email.send_keys('kethynayane816@gmail.com')

# Encontre o campo de senha e envie a senha
input_senha = browser.find_element(By.NAME, "password")
input_senha.send_keys('kethy123')
input_senha.send_keys(Keys.ENTER)

#Aguarde até que o botão da CAIXA DE CRIAÇÃO DE COMPRAS se torne clicável e clique nele
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/header/section[2]/div/header/button'))).click()


#Aguarde até que o botão de CALÇADOS se torne clicável e clique nele
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[2]'))).click()

input_campo_nome = browser.find_element(By.ID, "mui-2")
input_campo_nome.send_keys('Tênis')

input_descrição_produto = browser.find_element(By.ID, "mui-3")
input_descrição_produto.send_keys('Azul')

input_preço = browser.find_element(By.ID, "mui-4")
input_preço.send_keys('149,90')

button_enviar = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'mui-5')))
button_enviar.send_keys(r'C:\\images1.jpg')

input_preço = browser.find_element(By.ID, "mui-6")
input_preço.send_keys('14,00')
input_preço.send_keys(Keys.ENTER)


browser.quit()