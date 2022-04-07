# import shutil

arquivo = r"D:\Projetos\calculadora"
caminho = r"D:\Downloads\testeSaida"

# shutil.make_archive(caminho, 'zip', arquivo)
#############################################################################################################################################################################################################################################################


# Get the database using the method we defined in pymongo_test_insert file 
import models.arquivos as arquivos
from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text("Diretório de origem:"), sg.Input(key='origem'), sg.FileBrowse()],
    [sg.Text('Diretório de destino:'), sg.Input(key='destino'), sg.FileBrowse()],
    [sg.Button('Inserir', key='inserir')]
]

# Janela
janela = sg.Window('Backup management', layout)

# Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'inserir':
        arquivos.adicionar(valores['origem'], valores['destino'])
        print('inserido com sucesso')