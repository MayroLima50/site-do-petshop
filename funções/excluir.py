# função para exclusão de dados.

import streamlit as st
import sqlite3
import os

def excluir_pet(pet_id, foto_path):
    try:
        # 1. Conectar ao banco e remover o registro
        conn = sqlite3.connect('banco/petshop.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pets WHERE id = ?", (pet_id,))
        conn.commit()
        conn.close()

        # 2. Tentar apagar o arquivo de imagem da pasta
        if foto_path and os.path.exists(foto_path):
            os.remove(foto_path)

        st.success("Pet excluído com sucesso!")
        st.rerun() # Atualiza a tela para o pet sumir da lista
    except Exception as e:
        st.error(f"Erro ao excluir o pet: {e}")

def excluir_conta_usuario(usuario_id, foto_perfil_path):
    # Esta função pode ser usada na página de configurações futuramente
    try:
        conn = sqlite3.connect('banco/petshop.db')
        cursor = conn.cursor()
        
        # Opcional: Excluir todos os pets do usuário primeiro
        # cursor.execute("DELETE FROM pets WHERE dono_id = ?", (usuario_id,))
        
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
        conn.commit()
        conn.close()

        if foto_perfil_path and os.path.exists(foto_perfil_path):
            os.remove(foto_perfil_path)

        st.success("Sua conta foi removida.")
        st.session_state['logado'] = False
        st.rerun()
    except Exception as e:
        st.error(f"Erro ao excluir conta: {e}")