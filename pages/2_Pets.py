import streamlit as st
import os
from banco.db import buscar_pets_do_dono
from funções.cadastroPets import CadastroPet
# Importaremos as outras funções assim que criarmos os arquivos
# from funções.excluir import excluir_pet 

# Bloqueio de Segurança
if 'logado' not in st.session_state or not st.session_state['logado']:
    st.error("Acesso restrito!")
    st.stop()

usuario_id = st.session_state['usuario_atual'][0]

st.title("🐾 Meus Pets")

# 1. Área de Cadastro (Expander para economizar espaço)
with st.expander("➕ Cadastrar Novo Pet"):
    CadastroPet(usuario_id)

st.divider()

# 2. Listagem de Pets
pets = buscar_pets_do_dono(usuario_id)

if not pets:
    st.info("Você ainda não tem pets cadastrados.")
else:
    for pet in pets:
        # Criando um container para cada pet
        with st.container(border=True):
            col_img, col_info, col_acoes = st.columns([1, 2, 1])
            
            with col_img:
                if pet[6] and os.path.exists(pet[6]):
                    st.image(pet[6], use_container_width=True)
                else:
                    st.image("https://via.placeholder.com/150", caption="Sem foto")

            with col_info:
                st.subheader(pet[2]) # Nome do Pet
                st.write(f"**Espécie:** {pet[3]}")
                st.write(f"**Raça:** {pet[4]}")
                st.write(f"**Idade:** {pet[5]} anos")

            with col_acoes:
                st.write("---")
                if st.button(f"📝 Editar {pet[2]}", key=f"edit_{pet[0]}"):
                    st.session_state['pet_para_editar'] = pet
                    # Lógica para abrir modal de edição
                
                if st.button(f"🗑️ Excluir", key=f"del_{pet[0]}", type="secondary"):
                    # Chamaremos a função de excluir aqui
                    st.warning("Confirmar exclusão?")
