import pyautogui
import time
#from selecao_convenio import interact_with_screen
from initial_interface import executar_interface
from end_interface import executar_interface_finalizacao
from click_ok import clickOk
from empresa import comissaoEmpresa
from grupo import comissaoGrupo

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

while True:
  executar_interface()
  break
time.sleep(1)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

#Entrando no Yuppie
pyautogui.write("https://sistemayuppie.com.br/focopromotora/public/financeiro/pagar-comissao/")
pyautogui.press("enter")
time.sleep(2)

#Abrindo Menu
pyautogui.click(x=197, y=146, duration=0.5)
time.sleep(1)

#Abrindo Comissao Grupo
pyautogui.click(x=790, y=340, button="right", duration=0.5)
pyautogui.click(x=871, y=365, duration=0.5)

#Abrindo Comissao Empresa
pyautogui.click(x=490, y=340, duration=0.5)
time.sleep(3)

#COMISSAO EMPRESA
comissaoEmpresa()

#COMISSAO GRUPO
#Selecionar aba
pyautogui.click(x= 379, y=12, duration=0.5)
time.sleep(2)

comissaoGrupo()

executar_interface_finalizacao()


