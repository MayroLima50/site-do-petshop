import sqlite3

def criar_tabelas():
    conn = sqlite3.connect('banco/petshop.db')
    cursor = conn.cursor()
    
    # 1. Criação da Tabela de Usuários (Tutores)
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
    
    # 2. Tabela de Pets (vinculada ao dono_id)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dono_id INTEGER,
            nome_pet TEXT NOT NULL,
            especie TEXT,
            raca TEXT,
            idade_pet INTEGER,
            foto_pet_path TEXT,
            FOREIGN KEY (dono_id) REFERENCES usuarios (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Tabelas verificadas/criadas com sucesso!")