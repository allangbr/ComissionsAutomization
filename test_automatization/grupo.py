import pyautogui
import time
from click_ok import clickOk

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def comissaoGrupo():
  banco = []
  with open('txt/banco.txt', 'r') as arquivo:
    for linha in arquivo:
      banco.append(linha.split('\n')[0])

  convenios = []
  with open('txt/convenio.txt', 'r') as arquivo:
    for linha in arquivo:
      convenios.append(linha.split('\n')[0])

  tipos_produtos = []
  with open('txt/tipo_produto.txt', 'r') as arquivo:
    for linha in arquivo:
      tipos_produtos.append(linha.split('\n')[0])


  #Selecionar Banco
  pyautogui.click(x=371,y=251) 
  pyautogui.write(banco[0])
  pyautogui.press("enter")
  time.sleep(1)

  count_grupo = 0
  count_produto = 0
  teste_run = 0
  teste_run2 = 0

  for line in convenios:
    if count_grupo >= 1:
      pyautogui.click(x=146,y=302, duration=0.5)
      pyautogui.write(line)
      pyautogui.press("enter")

      for line_produto in tipos_produtos:
        #Seleciando Tipo
        pyautogui.click(x=152,y=333, duration=0.5)
        pyautogui.write(line_produto)
        pyautogui.press("enter")

        #Buscar
        pyautogui.click(x=35, y=484, duration=0.5)
        time.sleep(2)

        #Selecao Check
        pyautogui.click(x=1330, y=532, duration=0.5)
        pyautogui.press("end")

        #Ação
        clickOk()

      #Buscar
      pyautogui.click(x=35, y=484, duration=0.5)
      time.sleep(2)

      #Selecao Check
      pyautogui.click(x=1330, y=532, duration=0.5)
      pyautogui.press("end")

      #Ação
      clickOk()

    if count_grupo == 0:
      pyautogui.click(x=158,y=279, duration=0.5)
      pyautogui.write(line)
      pyautogui.press("enter")

      #Campo Comissoes Vigentes
      pyautogui.click(x=362,y=425, duration=0.5)
      pyautogui.press("s")
      pyautogui.press("enter")

      for line_produto in tipos_produtos:
        if count_produto == 0:
          #Seleciando Tipo
          pyautogui.click(x= 146, y= 307, duration=0.5)
          pyautogui.write(line_produto)
          pyautogui.press("enter")

          #Campo Busca
          pyautogui.click(x=37,y=461, duration=0.5)
          time.sleep(2)

          #Selecao Check
          pyautogui.click(x=1330, y=532, duration=0.5)
          pyautogui.press("end")

          #Ação
          clickOk()

          count_produto += 1
          teste_run += 1
          teste_run2 += 1

        #Seleciando Tipo
        pyautogui.click(x=152,y=333, duration=0.5)
        pyautogui.write(line_produto)
        pyautogui.press("enter")

        #Buscar
        pyautogui.click(x=35, y=484, duration=0.5)
        time.sleep(2)

        #Selecao Check
        pyautogui.click(x=1330, y=532, duration=0.5)
        pyautogui.press("end")

        #Ação
        clickOk()

      #Buscar
      pyautogui.click(x=36,y=462, duration=0.5)
      time.sleep(2)

      #Selecao Check
      pyautogui.click(x=1330, y=532, duration=0.5)
      pyautogui.press("end")

      #Ação
      clickOk()

    count_grupo += 1
    teste_run += 1
    teste_run2 += 1
  
  if teste_run == 0:
    for line in tipos_produtos:
      if count_produto >= 1:
        #Seleciando Tipo
        pyautogui.click(x=152,y=333, duration=0.5)
        pyautogui.write(line_produto)
        pyautogui.press("enter")

        #Buscar
        pyautogui.click(x=35, y=484, duration=0.5)
        time.sleep(2)

        #Selecao Check
        pyautogui.click(x=1330, y=532, duration=0.5)
        pyautogui.press("end")

        #Ação
        clickOk()
        teste_run2 += 1

      #Seleciando Tipo
      pyautogui.click(x= 146, y= 307, duration=0.5)
      pyautogui.write(line_produto)
      pyautogui.press("enter")

      #Campo Busca
      pyautogui.click(x=37,y=461, duration=0.5)
      time.sleep(2)

      #Selecao Check
      pyautogui.click(x=1330, y=532, duration=0.5)
      pyautogui.press("end")

      #Ação
      clickOk()

      count_produto += 1
      teste_run2 += 1

  if teste_run2 == 0:
    #Campo Busca
    pyautogui.click(x=37,y=461, duration=0.5)
    time.sleep(2)

    #Selecao Check
    pyautogui.click(x=1330, y=532, duration=0.5)
    pyautogui.press("end")

    #Ação
    clickOk()

if __name__ == '__main__':
  comissaoGrupo()
