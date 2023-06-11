import re

import sqlite3

conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()


def digitar_valor():
    
    while True:
        valor = input("\nDigite o valor da venda: ")
        if not re.match(r'^\d+(?:[.,]\d{2})?$', valor):
            print("Valor inválido. Digite um número no formato correto (ex: 10.00 ou 12,00).")
        else:
            return valor.replace(',', '.')
        
        
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


def consultar_melhor_loja(id_usuario):
    vendas_usuario = []
    total_valor = 0.0

    cursor.execute("SELECT * FROM vendas WHERE usuario = ?", (id_usuario,))
    resultados = cursor.fetchall()

    for venda in resultados:
        vendas_usuario.append(venda)
        total_valor += venda[5]

    conn.close()

    return vendas_usuario, total_valor