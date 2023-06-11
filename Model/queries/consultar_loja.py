
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

    conn.close()

    return vendas[0]