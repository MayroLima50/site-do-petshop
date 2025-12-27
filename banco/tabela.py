import sqlite3

def criar_tabelas():
    conn = sqlite3.connect('banco/petshop.db')
    cursor = conn.cursor()
    # criação da Tabela de Usuários destinadas aos Tutores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf TEXT UNIQUE,
            contato1 TEXT,
            contato2 TEXT,
            endereco TEXT,
            email TEXT UNIQUE,
            senha TEXT,
            foto_path TEXT
        )
    ''')
    conn.commit()
    conn.close()