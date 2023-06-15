
import socket
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

from Model.consultar_usuario import verificar_usuario
# from A3SD.Model.queries.adicionar_usuario import cadastrar_usuario
from Model.adicionar_venda import cadastrar_venda
from Model.consultar_venda import consultar_total_vendedor
from Model.consultar_loja import consultar_melhor_loja
from Model.consultar_usuario import consultar_melhor_vendedor
from Model.consultar_rede import consultar_vendas_rede

host = os.getenv('HOST')
port = 3333  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

def main():
    while True:
        server_socket.listen(1)
        print('Aguardando conexões...')

        client_socket, client_address = server_socket.accept()
        print('Conexão estabelecida com:', client_address)


        data = client_socket.recv(1024)
        if data == '':
            break
    
        dados_recebidos = data.decode()
        data_array = dados_recebidos.split(",")


        if data_array[0] == '01.1':
            get = verificar_usuario(data_array[1])
            if get[0] == True:
                response = get[0], get[1], get[2]
            elif get[0] == False:
                response = get[0]
            else:
                response = 'ERROR: Usuario desconhecido'
            
    # elif data_array[0] == '01.2':
    #     if cadastrar_usuario(data_array[2], data_array[3], data_array[4], data_array[5]):
    #         response = True, 'Usuario cadastrado com sucesso'
    #     else:
    #         response = False, 'ERROR: Usuario não foi cadastrado'
        
        elif data_array[0] == '02.0':
            if cadastrar_venda(data_array[2], data_array[3], data_array[4], data_array[5]):
                response = True, 'Venda cadastrada com sucesso'
            else: 
                response = False, 'ERROR: Venda não cadastrada'
            
        elif data_array[0] == '03.1':
            response = consultar_total_vendedor(data_array[2])
        elif data_array[0] == '03.2':
            response = consultar_melhor_loja()
        elif data_array[0] == '03.3':
            response = consultar_melhor_vendedor()
        elif data_array[0] == '03.4':
            response = consultar_vendas_rede(data_array[1], data_array[2], data_array[3])
        else:
            response = 'ERROR: Unknown message type ' + data_array[0]

        message_str = ','.join([str(item) for item in response])
        client_socket.send(message_str.encode())
    

        
    client_socket.close()
    server_socket.close()


main()

