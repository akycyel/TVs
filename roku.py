import os
import time



def limpar():
    os.system('clear')

def send_command(ip, command):
    print('/033[1;32msending../033[m')
    os.system(f'curl -v -X POST "http://{ip}:8060/{command}"')
    
def volume(ip, function, qtd):

     if function == 'down':
              for c in range(0, qtd):
                    send_command(ip, 'keypress/VolumeDown')
                    time.sleep(0.7)
     if function == 'up':
              for c in range(0, qtd):
                  send_command(ip, 'keypress/VolumeUp')
                  time.sleep(0.7)
def power(ip, opc):
    if opc == 'off':
        send_command(ip, 'keypress/PowerOff')
    elif opc == 'on':
        send_command(ip, 'keypress/PowerOn')
<F7>
def opc():
    limpar()
    t
    class basic_commands:
        
        print('debug/n')
        print('\033[1;34m[01] DESLIGAR TV\033[m')
        print('\033[1;32m[02] AUMENTAR VOLUME\033[m')
        print('\033[1;31m[03] DIMINUIR VOLUME\033[m')
        print('\033[1;34m[04] SAIR DE TUDO\033[m')

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
        
