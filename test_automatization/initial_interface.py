import PySimpleGUI as sg

def executar_interface():
  # Função para salvar os dados nos arquivos
  def salvar_dados(banco, convenios, tipos_produto):
    with open('txt/banco.txt', 'w') as f:
      f.write(banco)
    
    with open('txt/convenio.txt', 'w') as f:
      f.write('\n'.join(convenios))
    
    with open('txt/tipo_produto.txt', 'w') as f:
      f.write('\n'.join(tipos_produto))


  # Layout da interface
  layout = [
    [sg.Text('Banco'), sg.InputText(key='-BANCO-')],
    [sg.Text('Convenio'), sg.Listbox(values=[], size=(30, 6), key='-CONVENIOS-', select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE), sg.InputText(key='-CONVENIO-'), sg.Button('Adicionar Convenio')],
    [sg.Text('Tipo de Produto'), sg.Listbox(values=[], size=(30, 6), key='-TIPOS_PRODUTO-', select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE), sg.InputText(key='-TIPO_PRODUTO-'), sg.Button('Adicionar Tipo')],
    [sg.Button('OK'), sg.Button('Cancelar')]
  ]

  # Criar a janela
  window = sg.Window('Formulário de Dados', layout)

  convenios = []
  tipos_produto = []

  # Loop de eventos
  while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancelar':
      break
    elif event == 'Adicionar Convenio':
      novo_convenio = values['-CONVENIO-'].strip()
      if novo_convenio and novo_convenio not in convenios:
        convenios.append(novo_convenio)
        window['-CONVENIOS-'].update(convenios)
      window['-CONVENIO-'].update('')
    elif event == 'Adicionar Tipo':
      novo_tipo = values['-TIPO_PRODUTO-'].strip()
      if novo_tipo and novo_tipo not in tipos_produto:
        tipos_produto.append(novo_tipo)
        window['-TIPOS_PRODUTO-'].update(tipos_produto)
      window['-TIPO_PRODUTO-'].update('')
    elif event == 'OK':
      banco = values['-BANCO-'].strip()
      salvar_dados(banco, convenios, tipos_produto)
      sg.popup('Dados salvos com sucesso!')
      break

  # Fechar a janela
  window.close()

# Exemplo de uso no arquivo principal
if __name__ == '__main__':
  executar_interface()
