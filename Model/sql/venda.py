
import sqlite3
conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()

def inserir_venda(venda):
    cursor.execute(
        "INSERT INTO Vendas (idvenda, datavenda, usuario, loja, valor) VALUES (?, ?, ?, ?, ?)",
        (
            venda['idvenda'],
            venda['datavenda'],
            venda['usuario'],
            venda['loja'],
            venda.get('valor', None),
        ),
    )
    conn.commit()