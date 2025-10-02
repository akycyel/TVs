import os
import time

def send_command(ip, command):
    print('/033[1;32msending../033[m')
    os.system(f'curl -v -X POST "http://{ip}:8060/{command}"')
    
def volume(ip, function, qtd):

     if function == 'down':
              for c in range(0, qtd):
                    send_command(ip, 'keypress/VolumeDown')
                    time.sleep(0.7)
ip = '192.168.100.7'
f = 'down'
qtd = 10
volume(ip, f, qtd)



