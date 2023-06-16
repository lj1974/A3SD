
import sqlite3

conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()

def consultar_melhor_loja():
    vendas = []

    cursor.execute("""
        SELECT Vendas.idvenda, Lojas.nomeloja, Vendas.valor
        FROM Vendas
        INNER JOIN Lojas ON Vendas.loja = Lojas.idloja
        GROUP BY Vendas.loja
        ORDER BY Vendas.valor DESC
    """)

    vendas = cursor.fetchall()

    return vendas[0]




def obter_ids_por_nome(nome_loja):

    # Consultar o ID do usuário pelo nome
    cursor.execute("SELECT idloja FROM Lojas WHERE nomeloja = ?", (nome_loja,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0] 
    else:
        return None 