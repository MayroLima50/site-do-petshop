import streamlit as st
import os
from banco.db import buscar_pets_do_dono
from funções.cadastroPets import CadastroPet
from funções.excluir import excluir_pet
from funções.atualizar import atualizar_pet

# 1. Bloqueio de Segurança: Garante que só usuários logados acessem
if 'logado' not in st.session_state or not st.session_state['logado']:
    st.error("Acesso restrito! Por favor, faça login.")
    st.stop()

# Recupera o ID do usuário logado
usuario_id = st.session_state['usuario_atual'][0]

st.title("🐾 Meus Pets")

# 2. Área de Cadastro
with st.expander("➕ Cadastrar Novo Pet"):
    CadastroPet(usuario_id)

# 3. Lógica de Edição (Aparece no topo quando o botão editar é clicado)
# Corrigido para usar a chave correta 'pet_para_editar'
if 'pet_para_editar' in st.session_state:
    pet = st.session_state['pet_para_editar']
    
    with st.container(border=True):
        st.subheader(f"📝 Editando: {pet[2]}")
        with st.form("form_edicao"):
            nome = st.text_input("Nome", value=pet[2])
            
            # Opções de espécie para o selectbox
            opcoes_especie = ["Cão", "Gato", "Pássaro", "Outro"]
            # Tenta encontrar o índice da espécie atual para vir selecionado corretamente
            try:
                index_especie = opcoes_especie.index(pet[3])
            except ValueError:
                index_especie = 0
                
            especie = st.selectbox("Espécie", opcoes_especie, index=index_especie)
            raca = st.text_input("Raça", value=pet[4])
            idade = st.number_input("Idade", value=int(pet[5]))
            nova_foto = st.file_uploader("Trocar Foto (deixe vazio para manter a atual)", type=['png', 'jpg', 'jpeg'])
            
            col_bt1, col_bt2 = st.columns(2)
            
            if col_bt1.form_submit_button("Salvar Alterações"):
                # pet[0] é o ID e pet[6] é o caminho da foto antiga
                if atualizar_pet(pet[0], nome, especie, raca, idade, nova_foto, pet[6]):
                    st.success("Dados atualizados com sucesso!")
                    del st.session_state['pet_para_editar'] # Limpa o estado
                    st.rerun()
            
            if col_bt2.form_submit_button("Cancelar"):
                del st.session_state['pet_para_editar']
                st.rerun()

st.divider()

# 4. Listagem de Pets
pets = buscar_pets_do_dono(usuario_id)

if not pets:
    st.info("Você ainda não tem pets cadastrados.")
else:
    # Cria os cards para cada pet
    for pet in pets:
        with st.container(border=True):
            col_img, col_info, col_acoes = st.columns([1, 2, 1])
            
            with col_img:
                # pet[6] é o caminho da imagem no banco
                if pet[6] and os.path.exists(pet[6]):
                    st.image(pet[6], use_container_width=True)
                else:
                    st.image("https://via.placeholder.com/150", caption="Sem foto")

            with col_info:
                st.subheader(pet[2]) # Nome
                st.write(f"**Espécie:** {pet[3]}")
                st.write(f"**Raça:** {pet[4]}")
                st.write(f"**Idade:** {pet[5]} anos")

            with col_acoes:
                st.write("---")
                
                # BOTÃO EDITAR CORRIGIDO: 
                # Agora ele salva o objeto 'pet' completo e dá rerun para abrir o form acima
                if st.button(f"📝 Editar", key=f"edit_{pet[0]}"):
                    st.session_state['pet_para_editar'] = pet
                    st.rerun()

                # BOTÃO EXCLUIR
                with st.popover("🗑️ Excluir"):
                    st.warning(f"Deseja excluir {pet[2]}?")
                    if st.button("Sim, confirmar", key=f"conf_del_{pet[0]}"):
                        excluir_pet(pet[0], pet[6])
                        st.rerun()
                        