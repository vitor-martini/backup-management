import shutil
from os import path
from datetime import datetime
from PySimpleGUI import PySimpleGUI as sg

def inserir(origem, destino):
    f = open("arquivos.txt", "r+")
    f.write(str(len(f.readlines()) + 1) +' | ' + str(origem).replace('\\', '/') +' | ' + str(destino).replace('\\', '/') +'\n')
    f.close()

def excluir(lista_excluir):
    lista = []
    for item in lista_excluir:
        lista.append(int(item[0]))

    f = open("arquivos.txt", "r")
    lines = f.readlines()

    f = open("arquivos.txt", "w")
    for line in lines:        
        if int(line.partition("|")[0]) not in lista:
            f.write(line)
        
    f.close()

def carregar_lista():
    f = open("arquivos.txt", "r")
    list_of_lists = []
    for line in f:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    f.close()   
    return list_of_lists 

def backup():    
    data = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    lista = carregar_lista()
    for item in lista:
        if path.exists(item[2]):
            shutil.make_archive(item[4] + '-' + data, 'zip', item[2])
        else:
            sg.popup('O caminho [' + item[2] + '] do item ['+ item[0]+'] é inválido.')

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text("Diretório de origem:"), sg.Input(key='origem'), sg.FileBrowse()],
    [sg.Text('Diretório de destino:'), sg.Input(key='destino'), sg.FileBrowse()],
    [sg.Button('Inserir', key='inserir'), sg.Button('Excluir', key='excluir'), sg.Button('Executar backup', key='backup')],
    [sg.Listbox(key='lista', values = carregar_lista(),select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(70, 10))]
]

# Janela
janela = sg.Window('Backup management', layout)

# Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'inserir':
        inserir(valores['origem'], valores['destino'])
        janela.find_element('lista').update(values = load_list())
    if eventos == 'excluir':
        excluir(janela.find_element('lista').get())
        janela.find_element('lista').update(values = load_list())
    if eventos == 'backup':
        backup()


