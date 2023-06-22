
import socket
import os
import threading
from dotenv import load_dotenv

from Controller.login import realizar_login
from Modulos.modulo_servidor import modulo_servidor
from Modulos.modulo_servidor_temporario import is_servidor_ativo, iniciar_eleicao, connections
from View.users import coletar_dados_novo_usuario
from Controller.gerente import form_gerente
from Controller.vendedor import form_vendedor
from Model.consultar_usuario import obter_id_por_nome

load_dotenv()

host = os.getenv('HOST')
port = 3333  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

id = 0

def main():
    
    while True:
        print(connections)
        try:
            id = response_servidor()
            modulo_cliente()
    
        except ConnectionAbortedError or ConnectionError or ConnectionResetError as e:
            print('servidor offline. Aguarde um novo servidor assumir')
            start_server(id)


def start_server(id):
    elegido = iniciar_eleicao()
    
    if elegido == id:
        while True:
            print('\nSou o servidor temporario')
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((host, port))
            client_socket, client_address = server_socket.accept()
            # Cria uma nova thread para lidar com o cliente
            client_thread = threading.Thread(target=modulo_servidor, args=(client_socket,))
            client_thread.start()
            
            if is_servidor_ativo == True:
                break
    else:
        print("\nServidor substitutivo rodando...")
        print("\nId do servidor: " + elegido)

                
                


               
def response_servidor():
    try:
        response = client_socket.recv(1024)
    except (ConnectionAbortedError, ConnectionError, ConnectionResetError):
        print('Servidor offline. Aguarde um novo servidor assumir.')
        start_server(id)
        
    response = response.decode()
    response = response.split(",")
    return response

def enviar_message(message):
    print(message, '\n\n')
    if len(message) == 4 and not message[0] == '03.4':
        message_str = message
    elif message[0] == '03.4' :
        print(message)
        message_str = ','.join([str(item) for item in message])
    else:
        message_str = ','.join([str(item) for item in message])
    
    try:
        client_socket.send(message_str.encode())
    except (ConnectionAbortedError, ConnectionError, ConnectionResetError):
        print('Servidor offline. Aguarde um novo servidor assumir.')
        start_server(id)

        
    print('mensagem enviada', message_str)
    
    



def modulo_cliente():
    count = 0
    resp = []
    confirmacao  = ''
    
    while True:
        if count > 0:
            resp[0] = 'True'
            if confirmacao  == 's':
                break
        else:
            message = realizar_login()
            enviar_message(message)
            resp = response_servidor()
            count+=1 
                 
        if resp[0] == 'True':
            while True:
                data = atividade_inicial(resp)
                enviar_message(data)
                resp2 = response_servidor()
                print('\n\n', resp2)
                confirmacao = input('\nSair? (s/n)')
                if confirmacao.lower() == "s":
                    break
        elif resp[0] == 'False':
            cadastro = coletar_dados_novo_usuario(message[1])
            enviar_message(cadastro)
            resp3 = response_servidor()
            if resp3[0] == 'True':
                resp[0] = resp3[0]
                resp[1] = (obter_id_por_nome(cadastro[1]))
                resp.append = cadastro[1]
                resp.append(cadastro[4])
                print(resp)
            else:
                print("ERROR: Encerrando por falha, tente novamente.")
                break
               


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


    
main()
client_socket.close()


