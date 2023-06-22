import socket
import threading
import os
from dotenv import load_dotenv


from Modulos.modulo_servidor import modulo_servidor
from Modulos.modulo_servidor_temporario import is_servidor_ativo, connections

load_dotenv()
host = os.getenv('HOST')
port = 3333  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))



def main():
    server_socket.listen(5)  
    
    is_servidor_ativo = True
    
    try:
        while True:
            print('Aguardando conexões...')
            client_socket, client_address = server_socket.accept()
            print('Conexão estabelecida com:', client_address)
            
            # Cria uma nova thread para lidar com o cliente
            client_thread = threading.Thread(target=modulo_servidor, args=(client_socket,))
            client_thread.start()
            
    except ConnectionResetError:
        print('Conexão resetada pelo cliente: ', client_address)
        for item in connections:
            if client_address in item.keys():
                connections.remove(item)

    except KeyboardInterrupt:
        print('Servidor encerrado.')
        is_servidor_ativo = False
  
    except socket.error as e:
        print('Erro de socket:', e)
        is_servidor_ativo = False

  
  


main()

server_socket.close()