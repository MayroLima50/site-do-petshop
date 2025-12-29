# Arquivo destinado a função de adição de pet, onde o usuário colocar o nome, idade e uma foto de seu pet.

import streamlit as st
import sqlite3
import os

def CadastroPet(usuario_id):
    st.markdown("### 🐾 Cadastrar Novo Pet")
    
    with st.form("form_pet", clear_on_submit=True):
        nome = st.text_input("Nome do Pet")
        especie = st.selectbox("Espécie", ["Cão", "Gato", "Pássaro", "Outro"])
        raca = st.text_input("Raça")
        idade = st.number_input("Idade do Pet", min_value=0, max_value=30)
        foto = st.file_uploader("Foto do Pet", type=['png', 'jpg', 'jpeg'])
        
        btn_pet = st.form_submit_button("Salvar Pet")
        
        if btn_pet:
            if foto:
                # Salvar imagem na pasta de pets
                if not os.path.exists("fotos_pets"):
                    os.makedirs("fotos_pets")
                
                caminho_foto_pet = f"fotos_pets/{usuario_id}_{nome}_{foto.name}"
                with open(caminho_foto_pet, "wb") as f:
                    f.write(foto.getbuffer())
                
                # Inserir no banco
                conn = sqlite3.connect('banco/petshop.db')
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO pets (dono_id, nome_pet, especie, raca, idade_pet, foto_pet_path)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (usuario_id, nome, especie, raca, idade, caminho_foto_pet))
                conn.commit()
                conn.close()
                st.success(f"{nome} cadastrado com sucesso!")
                st.rerun() # Para atualizar a lista de pets na tela
            else:
                st.error("Por favor, envie uma foto do seu pet.")