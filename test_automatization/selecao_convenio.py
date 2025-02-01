from time import sleep
import pyautogui
import pytesseract
from PIL import Image

pyautogui.useImageNotFoundException(False)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# target_text = "PREF BELO HORIZONTE - MG"
# target_text_initial = target_text[0]

def capture_and_read_text(region=None):
  screenshot = pyautogui.screenshot(region=region)
  sleep(0.5)
  text = pytesseract.image_to_string(screenshot)
  return text

def find_text_on_screen(target_text, region=None, max_scrolls=50):
  scrolls = 0
  while scrolls < max_scrolls:
    text = capture_and_read_text(region)
    if target_text in text:
      return True
    pyautogui.press("down")
    scrolls += 1
  return False

def interact_with_screen(target_text, target_text_initial):
  sleep(5)
  pyautogui.click(x=244, y=297, duration=0.5)
  pyautogui.moveTo(x=588, y=320, duration=0.5)
  pyautogui.press("home")
  pyautogui.write(target_text_initial)

  selector_region = (182, 591, 419, 15)

  try:
    if find_text_on_screen(target_text, region=selector_region):
      print(f"Texto '{target_text}' encontrado na tela!")
      pyautogui.click(x=190, y=595, duration=0.5)

      # Aqui você pode adicionar código para clicar no item, se necessário
    else:
      print(f"Texto '{target_text}' não encontrado na tela.")
  except Exception as e:
    print(e)



# sleep(5)
# pyautogui.click(x=244, y=297, duration=0.5)
# pyautogui.moveTo(x=588, y=320, duration=0.5)
# pyautogui.press("home")
# pyautogui.write(target_text_initial)

# selector_region = (182, 591, 419, 15)

# try:
#   if find_text_on_screen(target_text, region=selector_region):
#     print(f"Texto '{target_text}' encontrado na tela!")
#     pyautogui.click(x=190, y=595, duration=0.5)

#     # Aqui você pode adicionar código para clicar no item, se necessário
#   else:
#     print(f"Texto '{target_text}' não encontrado na tela.")
# except Exception as e:
#   print(e)

# sleep(5)
# pyautogui.click(x=244, y=297, duration=0.5)
# pyautogui.moveTo(x=244, y=320, duration=0.5)
# pyautogui.press("home")

# location = pyautogui.locateCenterOnScreen('natal.png', confidence=0.8)

# while location == None:
#   pyautogui.scroll(-100)
#   sleep(1)
#   location = pyautogui.locateCenterOnScreen('natal.png', confidence=0.8)

# if location is not None:
#   pyautogui.click(location)
