import pyautogui
import time
from click_ok import clickOk

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def comissaoEmpresa():
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

  #Selecionando Banco
  pyautogui.click(x=131,y=250, duration=0.5)
  pyautogui.write(banco[0])
  pyautogui.press("enter")
  time.sleep(1)

  count = 0
  count_produto = 0
  teste_run = 0
  teste_run2 = 0

  for line in convenios:
    if count >= 1:
      pyautogui.click(x=140,y=301, duration=0.5)
      pyautogui.write(line)
      pyautogui.press("enter")
      time.sleep(0.5)

      for line_produto in tipos_produtos:
        #Seleciando Tipo
        pyautogui.click(x=364,y=270, duration=0.5)
        pyautogui.write(line_produto)
        pyautogui.press("enter")

        #Campo Busca
        pyautogui.click(x=33,y=430, duration=0.5)
        time.sleep(2)

        #Selecao Check
        pyautogui.click(x= 1330, y=475, duration=0.5)
        pyautogui.press("end")

        #Ação
        clickOk()

      #Campo Busca
      pyautogui.click(x=33,y=430, duration=0.5)

      #Selecao Check
      pyautogui.click(x= 1330, y=475, duration=0.5)
      pyautogui.press("end")

      #Ação
      clickOk()

    if count == 0:
      #Campo convenio
      pyautogui.click(x=134,y=281, duration=0.5)
      pyautogui.write(line)
      pyautogui.press("enter")
      time.sleep(0.5)

      #Campo Comissoes Vigentes
      pyautogui.click(x=363,y=311, duration=0.5)
      pyautogui.press("s")
      pyautogui.press("enter")

      for line_produto in tipos_produtos:
        if count_produto == 0:
          #Seleciando Tipo
          pyautogui.click(x= 364, y= 249, duration=0.5)
          pyautogui.write(line_produto)
          pyautogui.press("enter")

          #Campo Busca
          pyautogui.click(x=37,y=407, duration=0.5)
          time.sleep(2)

          #Selecao Check
          pyautogui.click(x= 1330, y=475, duration=0.5)
          pyautogui.press("end")

          #Ação
          clickOk()

          count_produto += 1
          teste_run += 1
          teste_run2 += 1

        #Seleciando Tipo
        pyautogui.click(x=364,y=270, duration=0.5)
        pyautogui.write(line_produto)
        pyautogui.press("enter")

        #Campo Busca
        pyautogui.click(x=33,y=430, duration=0.5)
        time.sleep(2)

        #Selecao Check
        pyautogui.click(x= 1330, y=475, duration=0.5)
        pyautogui.press("end")

        #Ação
        clickOk()

      #Campo Busca
      pyautogui.click(x=37,y=407, duration=0.5)
      time.sleep(2)

      #Selecao Check
      pyautogui.click(x= 1330, y=475, duration=0.5)
      pyautogui.press("end")

      #Ação
      clickOk()

    count += 1
    teste_run += 1
    teste_run2 += 1

  if teste_run == 0:
    for line_produto in tipos_produtos:
      if count_produto >= 1:
        #Seleciando Tipo
        pyautogui.click(x=364,y=270, duration=0.5)
        pyautogui.write(line_produto)
        pyautogui.press("enter")

        #Campo Busca
        pyautogui.click(x=33,y=430, duration=0.5)
        time.sleep(2)

        #Selecao Check
        pyautogui.click(x= 1330, y=475, duration=0.5)
        pyautogui.press("end")

        #Ação
        clickOk()

      #Seleciando Tipo
      pyautogui.click(x= 364, y= 249, duration=0.5)
      pyautogui.write(line_produto)
      pyautogui.press("enter")

      #Campo Busca
      pyautogui.click(x=37,y=407, duration=0.5)
      time.sleep(2)

      #Selecao Check
      pyautogui.click(x= 1330, y=475, duration=0.5)
      pyautogui.press("end")

      #Ação
      clickOk()

      count_produto += 1
      teste_run2 += 1

  if teste_run2 == 0:
    #Campo Busca
    pyautogui.click(x=37,y=407, duration=0.5)
    time.sleep(2)

    #Selecao Check
    pyautogui.click(x= 1330, y=475, duration=0.5)
    pyautogui.press("end")

    #Ação
    clickOk()

if __name__ == '__main__':
  comissaoEmpresa()