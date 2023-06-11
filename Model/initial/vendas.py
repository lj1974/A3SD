import uuid
import sqlite3

from A3SD.users import obter_id_por_nome as obterUsuarios
from A3SD.lojas import obter_id_por_nome as obterLojas


conn = sqlite3.connect('../onsell.db')
cursor = conn.cursor()


def obter_ids_usuarios():
    nomes_usuarios =  ['Maria das Dores', 'Pedro Solto Aguiar', 'João de Alencar', 'Ana Milena da Silva']
    ids_usuarios= tuple(obterUsuarios(nome) for nome in nomes_usuarios)
    return ids_usuarios

id_maria, id_pedro, id_joao, id_ana = obter_ids_usuarios() 


def obter_ids_lojas():
    nomes_lojas = ['Max Atacado Centro', 'Max Atacado Sul', 'Atakadão Norte', 'Atakadão Leste', 'Lojas Martins 1', 'Lojas Martins 2']
    ids_lojas= tuple(obterLojas(nome) for nome in nomes_lojas)
    return ids_lojas

maxcentro, maxsul, atakadaonorte, atakadaoleste, martinsum, martinsdois = obter_ids_lojas()

vendas_maria = [
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-01-17',
        'usuario_idusuario': id_maria,
        'loja_idloja': maxcentro, 
        'valor': 100.00
    },
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-02-10',
        'usuario_idusuario': id_maria,
        'loja_idloja':  maxsul, 
        'valor': 150.00
    },
]

vendas_pedro = [
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-01-17',
        'usuario_idusuario': id_pedro,
        'loja_idloja': atakadaoleste, 
        'valor': 250.00
    },
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-02-10',
        'usuario_idusuario': id_pedro,
        'loja_idloja': atakadaoleste, 
        'valor': 280.00
    },

]

vendas_joao = [
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-03-05',
        'usuario_idusuario': martinsdois,
        'loja_idloja': 'id_da_loja5',  
    },
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-04-20',
        'usuario_idusuario': martinsum,
        'loja_idloja': 'id_da_loja6',  
        'valor': 210.00
    },

]

vendas_ana = [
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-05-10',
        'usuario_idusuario': id_ana,
        'loja_idloja': atakadaonorte,  
        'valor': 150.00
    },
    {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-05-15',
        'usuario_idusuario': id_ana,
        'loja_idloja': maxsul,  
        'valor': 190.00
    },
     {
        'idvenda': str(uuid.uuid4()),
        'datavenda': '2023-03-01',
        'usuario_idusuario': id_ana,
        'loja_idloja': martinsdois,  
        'valor': 220.00
    },
  
]


# Função para inserir uma venda no banco de dados
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
