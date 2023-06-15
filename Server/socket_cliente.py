import socket

from Controller import login
from Model.queries.adicionar_usuario import cadastrar_usuario
from View.users import coletar_dados_novo_usuario
import gerente
import vendedor


host = '192.168.100.21'  
port = 3333  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))


def main():
   
    message = login()
    enviar_message(message)
    # Recebe a resposta do servidor
    response = client_socket.recv(1024)
        
    while True:
        if response[0] == True:
            if response[2] ==  'VENDEDOR':
                message2 = vendedor(response[1])
            elif response[2] == 'GERENTE':
                message2 = gerente(response[1])
            else:
                print("ERROR: unknown response")
                break
        
            enviar_message(message2)
            response2 = client_socket.recv(1024)
            dados_recebidos = response2.decode()
            data_array = dados_recebidos.split(",")
        elif response[0] == False:
            print("ERROR: Usuario inexistente")
        
            print(data_array)
        
    client_socket.close()


def enviar_message(message):
    message_str = ','.join([str(item) for item in message])
    print(message_str)
    client_socket.send(message_str.encode())