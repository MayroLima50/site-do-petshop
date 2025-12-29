#função para atualizar/editar dados.

import streamlit as st
import sqlite3
import os

def atualizar_pet(pet_id, nome_novo, especie_nova, raca_nova, idade_nova, foto_nova, foto_antiga_path):
    try:
        conn = sqlite3.connect('banco/petshop.db')
        cursor = conn.cursor()
        
        caminho_foto_final = foto_antiga_path

        # Verifica se o usuário carregou uma nova imagem
        if foto_nova is not None:
            # Remover a foto antiga do servidor para não acumular lixo
            if foto_antiga_path and os.path.exists(foto_antiga_path):
                os.remove(foto_antiga_path)
            
            # Salvar a nova foto
            if not os.path.exists("fotos_pets"):
                os.makedirs("fotos_pets")
            
            caminho_foto_final = f"fotos_pets/updated_{pet_id}_{foto_nova.name}"
            with open(caminho_foto_final, "wb") as f:
                f.write(foto_nova.getbuffer())

        # Atualizar o Banco de Dados
        cursor.execute('''
            UPDATE pets 
            SET nome_pet = ?, especie = ?, raca = ?, idade_pet = ?, foto_pet_path = ?
            WHERE id = ?
        ''', (nome_novo, especie_nova, raca_nova, idade_nova, caminho_foto_final, pet_id))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Erro ao atualizar: {e}")
        return False