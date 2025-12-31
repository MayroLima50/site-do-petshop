import streamlit as st
from banco.tabela import criar_tabelas
from funções.cadastroUsuario import CadastroUsuario
from banco.db import verificar_login

# 1. Tenta criar as tabelas sempre que o app inicia
try:
    criar_tabelas()
except Exception as e:
    st.error(f"Erro ao inicializar banco: {e}")

def tela_login():
    st.title("🐾PetZ")
    aba1, aba2 = st.tabs(["Acessar Conta", "Novo Cadastro"])
    
    with aba1:
        st.subheader("Login")
        email = st.text_input("E-mail", key="login_email")
        senha = st.text_input("Senha", type="password", key="login_senha")
        
        if st.button("Entrar"):
            # Verifica no banco de dados se o usuário existe
            usuario = verificar_login(email, senha)
            
            if usuario:
                st.session_state['logado'] = True
                st.session_state['usuario_atual'] = usuario
                st.success(f"Bem-vindo, {usuario[1]}!")
                st.rerun()
            else:
                st.error("E-mail ou senha incorretos.")
            
    with aba2:
        # Chama a função de cadastro que já criamos
        CadastroUsuario()

# --- LÓGICA DE NAVEGAÇÃO ---

if 'logado' not in st.session_state:
    st.session_state['logado'] = False

if not st.session_state['logado']:
    tela_login()
else:
    # Redireciona para a primeira página da pasta pages
    st.switch_page("pages/1_exibir.py")