import sqlite3

conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()


def listar_ids_e_nomes():

    # Consultar os IDs e nomes das redes
    cursor.execute("SELECT idrede, nomerede FROM Redes")
    resultados = cursor.fetchall()

    # Fechar a conexão
    conn.close()

    return resultados


def obter_id_por_nome(nome_rede):

    # Consultar o ID da rede pelo nome
    cursor.execute("SELECT idrede FROM Redes WHERE nomerede = ?", (nome_rede,))
    resultado = cursor.fetchone()

    # Fechar a conexão
    conn.close()

    if resultado:
        return resultado[0]
    else:
        return None
