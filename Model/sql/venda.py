
import sqlite3
conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()

def inserir_venda(venda):
    cursor.execute(
        "INSERT INTO Vendas (idvenda, datavenda, usuario_idusuario, loja_idloja, valor) VALUES (?, ?, ?, ?, ?)",
        (
            venda['idvenda'],
            venda['datavenda'],
            venda['usuario_idusuario'],
            venda['loja_idloja'],
            venda.get('valor', None),
        ),
    )
    conn.commit()