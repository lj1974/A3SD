
import sqlite3

conn = sqlite3.connect('Model/onsell.db')
cursor = conn.cursor()

def consultar_melhor_loja():
    vendas = []

    cursor.execute("""
        SELECT Vendas.idvenda, Lojas.nomeloja, SUM(valor) FROM Vendas
        JOIN Lojas ON Lojas.idloja = Vendas.loja
        GROUP BY Lojas.idloja
        ORDER BY SUM(valor) DESC
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