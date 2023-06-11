import sqlite3
import uuid

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('../../onsell.db')
cursor = conn.cursor()


# Dados dos funcionários
funcionarios = [
        {'idusuario': str(uuid.uuid4()), 'nomeusuario': 'João de Alencar', 'cpfusuario': '12345678901', 'anonascimento': '1990', 'cargousuario': 'VENDEDOR'},
        {'idusuario': str(uuid.uuid4()), 'nomeusuario': 'Maria das Dores', 'cpfusuario': '23456789012', 'anonascimento': '1995', 'cargousuario': 'VENDEDOR'},
        {'idusuario': str(uuid.uuid4()), 'nomeusuario': 'Pedro Solto Aguiar', 'cpfusuario': '34567890123', 'anonascimento': '1992', 'cargousuario': 'VENDEDOR'},
        {'idusuario': str(uuid.uuid4()), 'nomeusuario': 'Ana Milena da Silva', 'cpfusuario': '45678901234', 'anonascimento': '1993', 'cargousuario': 'VENDEDOR'},
        {'idusuario': str(uuid.uuid4()), 'nomeusuario': 'Lucas Matos de Abreu', 'cpfusuario': '56789012345', 'anonascimento': '1988', 'cargousuario': 'GERENTE'},
    ]

# Adicionar os funcionários
for funcionario in funcionarios:
        cursor.execute("INSERT INTO Usuarios (idusuario, nomeusuario, cpfusuario, anonascimento, cargousuario) VALUES (?, ?, ?, ?, ?)",
                       (funcionario['idusuario'], funcionario['nomeusuario'], funcionario['cpfusuario'], funcionario['anonascimento'], funcionario['cargousuario']))


# Salvar as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
