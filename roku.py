import os
import time



def text(txt):
    for c in txt:
        print(c, end="", flush=True)
        time.sleep(0.03)


def limpar():
    os.system('clear')

def send_command(ip, command):
    #print('/033[1;32msending../033[m')
    os.system(f'curl -v -X POST "http://{ip}:8060/{command}"')
    
def volume(ip, function, qtd):

     if function == 'down':
              for c in range(0, qtd):
                    send_command(ip, 'keypress/VolumeDown')
                    time.sleep(0.5)
     if function == 'up':
              for c in range(0, qtd):
                  send_command(ip, 'keypress/VolumeUp')
                  time.sleep(0.5)
def power(ip, opc):
    if opc == 'off':
        limpar()
        text('Desligando...')
        send_command(ip, 'keypress/PowerOff')
    elif opc == 'on':
        text('Ligando TV...')
        send_command(ip, 'keypress/PowerOn')

def opc():
    limpar()
    
    class basic_commands:
        
        print('debug/n')
        print('\033[1;34m[01] DESLIGAR TV\033[m')
        print('\033[1;32m[02] LIGAR TV\033[m')
        print('\033[1;31m[03] AUMENTAR VOLUME\033[m')
        print('\033[1;31m[04] DIMINUIR VOLUME\033[m')
        print('\033[1;34m[05] SAIR DE TUDO\033[m')

class home:
    
    text = 'Para começar, digite o ip: '
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.03)
    ip = input('')
    while True:
        opc()
        opc_ = input('Opção: ')
        if opc_ == 'sair':
            break
        elif opc_ == '1':
           limpar()
           power(ip, 'off')
        elif opc_ == '2':
            limpar()
            power(ip, 'on')
        elif opc_ == '3':
            limpar()
            #text('Quanto de volume pretende aumentar:')
            qtd = input('Quantidade de volume: ')
            fc = 'up'
            volume(ip, fc, qtd)
        elif opc == '4':
            limpar()


