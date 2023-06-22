import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('onsell.db')
cursor = conn.cursor()

# Cria a tabela Rede
cursor.execute('''
    CREATE TABLE Redes (
        idrede UUID PRIMARY KEY,
        nomerede VARCHAR(50)
    )
''')

# Cria a tabela Loja
cursor.execute('''
    CREATE TABLE Lojas (
        idloja UUID PRIMARY KEY,
        nomeloja VARCHAR(100),
        cnpjloja VARCHAR(14),
        redeloja UUID,
        FOREIGN KEY (redeloja) REFERENCES Redes (idrede)
    )
''')

# Cria a tabela Usuario
cursor.execute('''
    CREATE TABLE Usuarios (
        idusuario UUID PRIMARY KEY,
        nomeusuario VARCHAR(45),
        cpfusuario VARCHAR(11),
        anonascimento VARCHAR(4),
        cargousuario VARCHAR(50)
    )
''')

# Cria a tabela Venda
cursor.execute('''
    CREATE TABLE Vendas (
        idvenda UUID PRIMARY KEY,
        datavenda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        usuario UUID,
        loja UUID,
        valor DECIMAL(10, 2),
        FOREIGN KEY (usuario) REFERENCES Usuarios (idusuario),
        FOREIGN KEY (loja) REFERENCES Lojas (idloja)
    )
''')

# Salva as alterações e fecha a conexão com o banco de dados
conn.commit()
conn.close()
