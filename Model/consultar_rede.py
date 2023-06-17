
import sqlite3

conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()

def consultar_vendas_rede(rede, data_inicial, data_final):

    cursor.execute("""
    SELECT Vendas.idvendas, Vendas.datavenda, 
    Vendas.loja, Vendas.valor, Lojas.redeloja, Redes.nomerede
    FROM Vendas
    JOIN Lojas ON Vendas.loja = Lojas.idloja
    JOIN Redes ON Lojas.redeloja = Redes.idrede
    WHERE Vendas.datavenda BETWEEN ? AND ? AND Redes.idrede = ?
    GROUP BY Lojas.redeloja
""", (data_inicial, data_final, rede))

    resultados = cursor.fetchall()
    
    return resultados['nomerede'], resultados['valor']


def listar_ids_e_nomes():

    # Consultar os IDs e nomes das redes
    cursor.execute("SELECT idrede, nomerede FROM Redes")
    resultados = cursor.fetchall()


    return resultados


def obter_id_por_nome(nome_rede):

    # Consultar o ID da rede pelo nome
    cursor.execute("SELECT idrede FROM Redes WHERE nomerede = ?", (nome_rede,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0]
    else:
        return None



