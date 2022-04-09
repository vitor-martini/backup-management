import shutil
from os import path
from datetime import datetime
from PySimpleGUI import PySimpleGUI as sg

def inserir(origem, destino):
    if origem == '' or destino == '':
        sg.popup('Verifique as entradas.', title = 'Erro', icon='bkp.ico')
        return

    arquivo_backup = open('arquivos.txt', 'r+')
    arquivo_backup.write(str(len(arquivo_backup.readlines())) +' | ' + str(origem).replace('\\', '/') +' | ' + str(destino).replace('\\', '/') +'\n') # Armazena as entradas no arquivo.
    arquivo_backup.close()

def excluir(lista):
    if len(lista) == 0:
        sg.popup('Selecione algum registro para excluir.', title = 'Erro', icon='bkp.ico')
        return

    # Exclui o cabeçalho
    if lista[0][0] == 'ID':
        lista.pop(0)

    # Recebe apenas os ID's
    lista = [int(item[0]) for item in lista]  

    # Recebe as linhas do arquivo
    arquivo_backup = open('arquivos.txt', 'r')
    linhas = arquivo_backup.readlines()
    arquivo_backup.close()

    # Sobre escreve o arquivo sem as linhas selecionadas
    arquivo_backup = open('arquivos.txt', 'w')
    for linha in linhas:        
        try:
            if int(linha.split('|')[0]) not in lista:
                arquivo_backup.write(linha)
        except:
            arquivo_backup.write(linha)
        
    arquivo_backup.close()

def carregar_lista():
    arquivo_backup = open('arquivos.txt', 'r')    
    lista = [linha for linha in arquivo_backup]
    arquivo_backup.close()   
    return lista 

def realizar_backup():    
    data = datetime.now().strftime('%Y-%m-%d--%H-%M-%S')  
    arquivo_backup = open('arquivos.txt', 'r')
    i = 0
    
    for linha in arquivo_backup:       
        if i == 0: # Pula a linha de cabeçalho
            i = 1
        else:
            id = linha.split('|')[0]
            arquivo_original = linha.split('|')[1].strip() 
            arquivo_backup = linha.split('|')[2].strip() + '/backup-' + data
            if path.exists(arquivo_original):
                shutil.make_archive(arquivo_backup , 'zip', arquivo_original)
            else:
                sg.popup('Operação cancelada. O caminho [' + arquivo_original + '] do item ['+ id +'] é inválido.', title = 'Erro', icon='bkp.ico')
                return

    sg.popup('Operação realizada com sucesso.', title = 'Sucesso', icon='bkp.ico')
    

def interface():
    # Layout
    layout = [
        [sg.Text('Arquivo original:'), sg.Input(key='origem', do_not_clear=False, size=(125,25)), sg.FolderBrowse()],
        [sg.Text('Arquivo backup:'), sg.Input(key='destino', do_not_clear=False, size=(125,25)), sg.FolderBrowse()],
        [sg.Button('Inserir', key='inserir'), sg.Button('Excluir', key='excluir'), sg.Button('Executar backup', key='backup')],
        [sg.Listbox(key='lista', values = carregar_lista(),select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(150, 25))]
    ]

    # Janela
    janela = sg.Window('Backup management', icon='bkp.ico').Layout(layout)

    # Ler eventos
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'inserir':
            inserir(valores['origem'], valores['destino'])
            janela.find_element('lista').update(values = carregar_lista()) # Recarrega grid
        if eventos == 'excluir':
            excluir(janela.find_element('lista').get())
            janela.find_element('lista').update(values = carregar_lista()) # Recarrega grid
        if eventos == 'backup':
            realizar_backup()

if (__name__ == "__main__"):
    interface()
