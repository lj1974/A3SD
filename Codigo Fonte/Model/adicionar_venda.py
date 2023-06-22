
# import sqlite3
import uuid

# conn = sqlite3.connect('Model/onsell.db')
# cursor = conn.cursor()    

def cadastrar_venda(cursor, data):

    vendas = {
            'idvenda': str(uuid.uuid4()),
            'datavenda': data[1],
            'usuario': data[4],
            'loja': data[2],
            'valor': data[3],
    }
    
    
    inserir_venda(cursor, vendas) 
    
    return True


def inserir_venda(cursor, venda):
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


    
    