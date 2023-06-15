
import sqlite3

conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()    

def consultar_total_vendedor(id_usuario):
    vendas_usuario = []
    total_valor = 0.0

    cursor.execute("SELECT * FROM vendas WHERE usuario = ?", (id_usuario,))
    resultados = cursor.fetchall()

    for venda in resultados:
        vendas_usuario.append(venda)
        total_valor += venda[5]

    conn.close()

    return vendas_usuario, total_valor


