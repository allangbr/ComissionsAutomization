import pyautogui
import time
import cv2
from datetime import datetime, timedelta

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def clickOk():
  # Obter a data de hoje
  hoje = datetime.now()

  # Calcular a data do dia anterior
  dia_anterior = hoje - timedelta(days=1)

  # Formatá-la como uma string no formato DDMMYYYY
  data_formatada = dia_anterior.strftime('%d%m%Y')

  local = pyautogui.locateCenterOnScreen('img/campo_acao.png', confidence=0.7)
  pyautogui.click(local, duration=0.3)

  pyautogui.press("s")
  pyautogui.press("enter")

  pyautogui.press("tab")
  pyautogui.write(data_formatada)

  pyautogui.press("tab")
  pyautogui.press("enter")
  time.sleep(2.5)

  # local_acao = pyautogui.locateCenterOnScreen("img/acao.png", confidence=0.7)
  # pyautogui.click(local_acao, duration=0.3)
  # time.sleep(0.3)

  # pyautogui.scroll(-100)

  # data = pyautogui.locateCenterOnScreen("img/data.png", confidence=0.7)
  # pyautogui.click(data, duration=0.3)
  # pyautogui.write(data_formatada)

  # ok = pyautogui.locateCenterOnScreen("img/ok.png", confidence=0.75)
  # pyautogui.click(ok, duration=0.3)
  # time.sleep(2)

if __name__ == '__main__':
  clickOk()

