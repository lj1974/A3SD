
import sqlite3
import uuid

from A3SD.Model.sql.venda import inserir_venda

conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()    

def cadastrar_venda(data, loja, valor, usuario):
    vendas = [
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': data,
        'usuario_idusuario': usuario,
        'loja_idloja': loja, 
        'valor': valor
    }]
    
    inserir_venda(vendas)
    # Fechar a conexão
    conn.close()
    
    return True

    
    