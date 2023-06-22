import sqlite3

from Model.consultar_usuario import verificar_usuario
from Model.adicionar_venda import cadastrar_venda
from Model.consultar_venda import consultar_total_loja, consultar_total_vendedor
from Model.consultar_loja import consultar_melhor_loja
from Model.consultar_usuario import consultar_melhor_vendedor
from Model.consultar_rede import consultar_vendas_rede
from Model.adicionar_usuario import cadastrar_usuario

from Modulos.modulo_servidor_temporario import atribuir_id_processo, connections

def modulo_servidor(client_socket):
     # Cria uma nova conexão com o banco de dados
    db_connection = sqlite3.connect('Model/onsell.db')
    cursor = db_connection.cursor()
    
    id = atribuir_id_processo()
    print('\nNovo ID atribuido: ', id)
    connections.append(id)
    print('\n\n', connections)
    
    client_socket.send(str(id).encode())
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        dados_recebidos = data.decode()
        data_array = dados_recebidos.split(",")

        if data_array[0] == '01.1':
            get = verificar_usuario(cursor, data_array[1])
            if get[0]:
                response = get
            elif not get[0]:
                response = get
            else:
                response = 'ERROR: Nada encontrado'

        elif data_array[0] == '02.0':
            if cadastrar_venda(cursor, data_array):
                db_connection.commit()
                response = True, 'Venda cadastrada com sucesso'
            else: 
                response = False, 'ERROR: Venda não cadastrada'

        elif data_array[0] == '03.1':
            response = consultar_total_vendedor(cursor, data_array[1], data_array[2])
        elif data_array[0] == '03.2':
            response = consultar_melhor_loja(cursor)
        elif data_array[0] == '03.3':
            response = consultar_melhor_vendedor(cursor)
        elif data_array[0] == '03.4':
            response = consultar_vendas_rede(cursor, data_array[1], data_array[2], data_array[3])
        elif data_array[0] == '03.5':
            response = consultar_total_loja(cursor, data_array[1], data_array[2])
        elif data_array[0] == '04.0':
            if cadastrar_usuario(cursor, data_array):
                db_connection.commit()
                response = True, 'Usuario cadastrado com sucesso'
            else: 
                response = False, 'ERROR: Usuario não cadastrada'
        else:
            print('ERROR: Unknown message type' + data_array[0])
            response = ''

        if not isinstance(response, bool):
            message_str = ','.join([str(item) for item in response])
        else:
            message_str = [str(response[0])]
            message_str.extend(response[1:])
            message_str = ','.join(message_str)

        client_socket.send(message_str.encode())
        print("messagem enviada: ", message_str)
        
        # Fecha o cursor e a conexão com o banco de dados
    cursor.close()
    db_connection.close()
   
   

