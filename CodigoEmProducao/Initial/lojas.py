import sqlite3
import uuid



conn = sqlite3.connect('../Model/onsell.db')
cursor = conn.cursor()

def obter_id_por_nome(nome_rede):

    # Consultar o ID da rede pelo nome
    cursor.execute("SELECT idrede FROM Redes WHERE nomerede = ?", (nome_rede,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0]
    else:
        return None

def obter_ids_redes():
    nomes_redes = ['MAX ATACADO', 'ATAKADAO', 'LOJAS MARTINS']
    ids_redes = tuple(obter_id_por_nome(nome) for nome in nomes_redes)
    return ids_redes


maxatacado, atakadao, lojamartins = obter_ids_redes()

lojas = [
    {'idloja': str(uuid.uuid4()), 'nomeloja': 'Max Atacado Centro', 'cnpjloja': '12345678000101', 'redeloja': maxatacado},
    {'idloja': str(uuid.uuid4()), 'nomeloja': 'Max Atacado Sul', 'cnpjloja': '23456789000102', 'redeloja': maxatacado},
    {'idloja': str(uuid.uuid4()), 'nomeloja': 'Atakadão Norte', 'cnpjloja': '34567890000103', 'redeloja': atakadao},
    {'idloja': str(uuid.uuid4()), 'nomeloja': 'Atakadão Leste', 'cnpjloja': '45678901000104', 'redeloja': atakadao},
    {'idloja': str(uuid.uuid4()), 'nomeloja': 'Lojas Martins 1', 'cnpjloja': '56789010000105', 'redeloja': lojamartins},
    {'idloja': str(uuid.uuid4()), 'nomeloja': 'Lojas Martins 2', 'cnpjloja': '67890101000106', 'redeloja': lojamartins},
]

# Adicionar as lojas
for loja in lojas:
    cursor.execute("INSERT INTO Lojas (idloja, nomeloja, cnpjloja, redeloja) VALUES (?, ?, ?, ?)", (loja['idloja'], loja['nomeloja'], loja['cnpjloja'], loja['redeloja']))


# Salvar as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
