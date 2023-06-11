import sqlite3

conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()

def verificar_usuario(cpf):
    # Aqui você pode implementar a lógica para verificar se o CPF corresponde a um cliente existente
    # Pode ser uma consulta em um banco de dados ou algum outro meio de armazenamento dos dados dos clientes
    # Neste exemplo, sempre retorna True para simular um cliente existente
    return True



    
def listar_ids_e_nomes():

    # Consultar os IDs e nomes dos usuários
    cursor.execute("SELECT idusuario, nomeusuario FROM Usuarios")
    resultados = cursor.fetchall()

    # Fechar a conexão
    conn.close()

    return resultados

def obter_id_por_nome(nome_usuario):

    # Consultar o ID do usuário pelo nome
    cursor.execute("SELECT idusuario FROM Usuarios WHERE nomeusuario = ?", (nome_usuario,))
    resultado = cursor.fetchone()

    # Fechar a conexão
    conn.close()

    if resultado:
        return resultado[0] 
    else:
        return None 


def consultar_melhor_vendedor():
    vendas = []

    cursor.execute("""
        SELECT Vendas.idvenda, Usuario.nomeusuario, Vendas.valor
        FROM Vendas
        INNER JOIN Lojas ON Vendas.usuario = Usuario.idusuario
        GROUP BY Vendas.usuario
        ORDER BY Vendas.valor DESC
    """)

    vendas = cursor.fetchall()

    conn.close()

    return vendas[0]