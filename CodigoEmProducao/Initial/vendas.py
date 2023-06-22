import uuid
import sqlite3


conn = sqlite3.connect('../Model/onsell.db')
cursor = conn.cursor()


def obter_usuario_por_nome(nome_usuario):

    # Consultar o ID do usuário pelo nome
    cursor.execute("SELECT idusuario FROM Usuarios WHERE nomeusuario = ?", (nome_usuario,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0] 
    else:
        return None 
    

def obter_loja_por_nome(nome_loja):

    # Consultar o ID do usuário pelo nome
    cursor.execute("SELECT idloja FROM Lojas WHERE nomeloja = ?", (nome_loja,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0] 
    else:
        return None 


def obter_ids_usuarios():
    nomes_usuarios =  ['Maria das Dores', 'Pedro Solto Aguiar', 'João de Alencar', 'Ana Milena da Silva']
    ids_usuarios= tuple(obter_usuario_por_nome(nome) for nome in nomes_usuarios)
    return ids_usuarios

id_maria, id_pedro, id_joao, id_ana = obter_ids_usuarios() 


def obter_ids_lojas():
    nomes_lojas = ['Max Atacado Centro', 'Max Atacado Sul', 'Atakadão Norte', 'Atakadão Leste', 'Lojas Martins 1', 'Lojas Martins 2']
    ids_lojas= tuple(obter_loja_por_nome(nome) for nome in nomes_lojas)
    return ids_lojas

maxcentro, maxsul, atakadaonorte, atakadaoleste, martinsum, martinsdois = obter_ids_lojas()

vendas_maria = [
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-01-17',
        'usuario': id_maria,
        'loja': maxcentro, 
        'valor': 100.00
    },
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-02-10',
        'usuario': id_maria,
        'loja':  maxsul, 
        'valor': 150.00
    },
]

vendas_pedro = [
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-01-17',
        'usuario': id_pedro,
        'loja': atakadaoleste, 
        'valor': 250.00
    },
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-02-10',
        'usuario': id_pedro,
        'loja': atakadaoleste, 
        'valor': 280.00
    },

]

vendas_joao = [
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-03-05',
        'usuario': id_joao,
        'loja': martinsdois,  
        'valor': 120.00
    },
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-04-20',
        'usuario': id_joao,
        'loja': martinsum,  
        'valor': 210.00
    },

]

vendas_ana = [
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-05-10',
        'usuario': id_ana,
        'loja': atakadaonorte,  
        'valor': 150.00
    },
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-05-15',
        'usuario': id_ana,
        'loja': maxsul,  
        'valor': 190.00
    },
     {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-03-01',
        'usuario': id_ana,
        'loja': martinsdois,  
        'valor': 220.00
    },
  
]

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
    
# Vendas da Maria
for venda in vendas_maria:
    inserir_venda(venda)

# Vendas do Pedro
for venda in vendas_pedro:
    inserir_venda(venda)

# Vendas do João
for venda in vendas_joao:
    inserir_venda(venda)

# Vendas da Ana
for venda in vendas_ana:
    inserir_venda(venda)

# Fechar a conexão
conn.close()
