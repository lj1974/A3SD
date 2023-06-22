
import socket
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

from Controller.login import realizar_login
from Controller.gerente import form_gerente
from Controller.vendedor import form_vendedor


host = os.getenv('HOST')
port = 3333  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))


def enviar_message(message):
    if len(message) == 4 and not message[0] == '03.4':
        message_str = message
    elif message[0] == '03.4' :
        print(message)
        message_str = ','.join([str(item) for item in message])
    else:
        message_str = ','.join([str(item) for item in message])
        
    client_socket.send(message_str.encode())
    print('mensagem enviada', message_str)



def response_servidor():
    response = client_socket.recv(1024)
    response = response.decode()
    response = response.split(",")
    return response

def atividade_inicial(response):
    
    if response[0] == 'True':
        if response[3] ==  'VENDEDOR':
            form = list(form_vendedor(response[2])) 
            form.append(response[1])
            return form
        elif response[3] == 'GERENTE':
            form = form_gerente(response[2])
            return form
        else:
            print("ERROR: unknown response")
            return ''
    
        
    elif response[0] == 'False':
        print("ERROR: Usuario inexistente")
        return ''
    else:
        print(response)
        return ''

        
def main():
    message = realizar_login()
    enviar_message(message)
    resp = response_servidor()
    
    while True:
        data = atividade_inicial(resp)
        enviar_message(data)
        resp2 = response_servidor()
        print('\n\n', resp2)
        confirmacao = input('\nSair? (s/n)')
        if confirmacao.lower() == "s":
            break
        



main()

client_socket.close()