import sqlite3
import uuid

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('../../onsell.db')
cursor = conn.cursor()

# Adicionar 3 redes diferentes
redes = [
    {'idrede': str(uuid.uuid4()), 'nomerede': 'MAX ATACADO'},
    {'idrede': str(uuid.uuid4()), 'nomerede': 'ATAKADAO'},
    {'idrede': str(uuid.uuid4()), 'nomerede': 'LOJAS MARTINS'}
]

for rede in redes:
    cursor.execute("INSERT INTO Redes (idrede, nomerede) VALUES (?, ?)", (rede['idrede'], rede['nomerede']))


# Salvar as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()