import sqlite3

conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()

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
    
    return resultado




def escolher_vendedor():
   
   while True:
        print("\n\nLista de Vendedores:\n")
        vendedor = listar_ids_e_nomes()
        for i, vendedor in enumerate(vendedor, start=1):
            print(f"{i}. {vendedor['nomeloja']}")

    
        num_vendedor = int(input("\nDigite o número do Vendedor: "))
        if num_vendedor < 1 or num_vendedor > len(vendedor):
            print("Número do vendedor inválido. Tente novamente.")
        else:
            return vendedor[num_vendedor - 1]
        
    
