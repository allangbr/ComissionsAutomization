import PySimpleGUI as sg

def executar_interface_finalizacao():
    # Layout da interface
    layout = [
        [sg.Text('A aplicação foi finalizada.')],
        [sg.Button('OK')]
    ]

    # Criar a janela
    window = sg.Window('Finalização', layout)

    # Loop de eventos
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'OK':
            break

    # Fechar a janela
    window.close()

# Exemplo de uso no arquivo principal
if __name__ == '__main__':
    executar_interface_finalizacao()