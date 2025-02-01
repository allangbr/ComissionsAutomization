from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:/Users/Administrador/AppData/Local/Google/Chrome/User Data/Default")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://sistemayuppie.com.br/focopromotora/public/financeiro/pagar-comissao/")
# element = driver.find_element(By.XPATH, '//*[@id="nav-second"]/ul/li[2]/a')
# element.click()

time.sleep(60)
driver.quit()

