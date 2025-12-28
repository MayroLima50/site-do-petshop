import streamlit as st
from funções.cadastroUsuario import CadastroUsuario
from banco.db import verificar_login # Importando a nova função

def tela_login():
    st.title("🐾 Bem-vindo ao PetShop")

    aba_login, aba_cadastro = st.tabs(["Fazer Login", "Criar Conta"])

    with aba_login:
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        
        if st.button("Entrar"):
            # CHAMADA DA LÓGICA DE VERIFICAÇÃO
            dados_usuario = verificar_login(email, senha)
            
            if dados_usuario:
                st.session_state['logado'] = True
                # Guardamos os dados do usuário (nome, foto, etc) para usar no exibir.py
                st.session_state['usuario_atual'] = dados_usuario
                st.success(f"Bem-vindo, {dados_usuario[1]}!") # O índice 1 é o Nome no banco
                st.rerun()
            else:
                st.error("E-mail ou senha incorretos. Tente novamente.")

    with aba_cadastro:
        CadastroUsuario()