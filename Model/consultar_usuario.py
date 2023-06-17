import sqlite3

conn = sqlite3.connect('Model\onsell.db')
cursor = conn.cursor()

def verificar_usuario(cpf):
    
    cursor.execute("SELECT * FROM Usuarios WHERE cpfusuario = ?", (cpf,))
    resultado = cursor.fetchone()

    print(resultado)
    if resultado is not None:
        id_usuario = resultado[0]
        nome_usuario = resultado[1]
        funcao = resultado[4]
        return True, id_usuario, nome_usuario, funcao
    else:
        return False, 'None'




    
def listar_ids_e_nomes():

    # Consultar os IDs e nomes dos usuários
    cursor.execute("SELECT idusuario, nomeusuario FROM Usuarios")
    resultados = cursor.fetchall()

    return resultados

def listar_ids_e_nomes_vendedores():
    cursor.execute("SELECT idusuario, nomeusuario FROM Usuarios where cargousuario = 'VENDEDOR'")
    resultados = cursor.fetchall()

    return resultados
    
def obter_id_por_nome(nome_usuario):

    # Consultar o ID do usuário pelo nome
    cursor.execute("SELECT idusuario FROM Usuarios WHERE nomeusuario = ?", (nome_usuario,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0] 
    else:
        return None 


def consultar_melhor_vendedor():
    vendas = []

    cursor.execute("""
    SELECT Vendas.usuario, Usuarios.nomeusuario, SUM(Vendas.valor) AS total
    FROM Vendas
    INNER JOIN Usuarios ON Vendas.usuario = Usuarios.idusuario
    GROUP BY Vendas.usuario, Usuarios.nomeusuario
    ORDER BY total DESC;
    """)

    vendas = cursor.fetchall()


    return vendas[0]