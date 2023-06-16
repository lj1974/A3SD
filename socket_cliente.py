
import socket
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

from Controller.login import realizar_login
from Model.adicionar_usuario import cadastrar_usuario
from View.users import coletar_dados_novo_usuario
from Controller.gerente import form_gerente
from Controller.vendedor import form_vendedor


host = os.getenv('HOST')
port = 3333  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))


def main():
   
    message = realizar_login()
    enviar_message(message)
    # Recebe a resposta do servidor
    response = client_socket.recv(1024)
    response = response.decode()
    response = response.split(",")
    print(response)
    while True:
        if response[0] == 'True':
            if response[2] ==  'VENDEDOR':
                message2 = form_vendedor(response[1])
            elif response[2] == 'GERENTE':
                message2 = form_gerente(response[1])
            else:
                print("ERROR: unknown response")
                break
        
            enviar_message(message2)
            response2 = client_socket.recv(1024)
            dados_recebidos = response2.decode()
            data_array = dados_recebidos.split(",")
        elif response[0] == 'False':
            print("ERROR: Usuario inexistente")
            break
        else:
            print(response)
            break
        
         
        
    client_socket.close()


def enviar_message(message):
    message_str = ','.join([str(item) for item in message])
    client_socket.send(message_str.encode())
    
    
main() 