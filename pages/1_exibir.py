# importa as funções e sintaxes do streamlit.
import streamlit as st

if 'logado' not in st.session_state or not st.session_state['logado']:
    st.warning("Por favor, faça login para acessar esta página.")
    st.stop()

import streamlit as st
import os

# Bloqueio de segurança (Coloque isso no topo de todas as páginas da pasta /pages tbm)
if 'logado' not in st.session_state or not st.session_state['logado']:
    st.error("Acesso restrito! Por favor, faça login.")
    st.stop()

# Recuperando os dados que salvamos no login
# Se o seu SELECT foi "SELECT *", a ordem costuma ser:
# 0: id, 1: nome, 2: idade, 3: cpf, 4: contato1, 5: contato2, 6: endereco, 7: email, 8: senha, 9: foto_path
dados = st.session_state['usuario_atual']

st.title(f"Painel do Tutor: {dados[1]}")

# Criando colunas para organizar a UI
col_foto, col_info = st.columns([1, 2])

with col_foto:
    caminho_foto = dados[9]
    if caminho_foto and os.path.exists(caminho_foto):
        st.image(caminho_foto, width=200, caption="Foto de Identificação")
    else:
        st.warning("Foto não encontrada.")

with col_info:
    st.subheader("Informações Pessoais")
    st.write(f"**Idade:** {dados[2]} anos")
    st.write(f"**CPF:** {dados[3]}")
    st.write(f"**Contatos:** {dados[4]} / {dados[5]}")
    st.write(f"**Endereço:** {dados[6]}")

st.divider()

# Botão de Logout no menu lateral
if st.sidebar.button("Sair"):
    st.session_state['logado'] = False
    st.session_state['usuario_atual'] = None
    st.rerun()

