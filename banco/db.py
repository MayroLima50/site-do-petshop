import sqlite3

def verificar_login(email, senha):
    conn = sqlite3.connect('banco/petshop.db')
    cursor = conn.cursor()
    
    # Procuramos o usuário que tenha o e-mail E a senha informados
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone() # Pega a primeira linha encontrada
    
    conn.close()
    
    # Se 'usuario' não for None, significa que encontrou os dados certos
    return usuario

def buscar_pets_do_dono(usuario_id):
    conn = sqlite3.connect('banco/petshop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pets WHERE dono_id = ?", (usuario_id,))
    pets = cursor.fetchall()
    conn.close()
    return pets