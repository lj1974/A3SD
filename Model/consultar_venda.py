
import sqlite3

conn = sqlite3.connect('Model/onsell.db')
cursor = conn.cursor()    

def consultar_total_vendedor(id_usuario):
    vendas_usuario = []
    total_valor = 0.0

    cursor.execute("SELECT * FROM Vendas WHERE usuario = ?", (id_usuario,))
    resultados = cursor.fetchall()

    for venda in resultados:
        total_valor += venda[4]
    
    vendas_usuario = 'O valor total vendido pelo vendedor foi: ', total_valor

    return vendas_usuario


