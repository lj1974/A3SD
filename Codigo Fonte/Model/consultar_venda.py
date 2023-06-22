
# import sqlite3

# conn = sqlite3.connect('Model/onsell.db')
# cursor = conn.cursor()    

def consultar_total_loja(cursor, id_loja, nome_loja):
    vendas_loja = []
    total_valor = 0.0
    
    cursor.execute("SELECT * FROM Vendas where Loja = ?", (id_loja,))
    resultados = cursor.fetchall()
    
    for venda in resultados:
        total_valor += venda[4]
        
    vendas_loja = 'O total de vendas da loja ' + nome_loja + ' foi: ', total_valor
    
    return vendas_loja


def consultar_total_vendedor(cursor, id_usuario, nome_usuario):
    vendas_usuario = []
    total_valor = 0.0

    cursor.execute("SELECT * FROM Vendas WHERE usuario = ?", (id_usuario,))
    resultados = cursor.fetchall()

    for venda in resultados:
        total_valor += venda[4]
    
    vendas_usuario = 'O valor total vendido pelo vendedor ' + nome_usuario +  ' foi: ', total_valor

    return vendas_usuario


