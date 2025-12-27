# Pasta main(principal)
import streamlit as st
from banco.tabela import criar_tabelas
from funções.cadastroUsuario import CadastroUsuario

# Inicializa o banco ao abrir o app
criar_tabelas()

st.title("🐾 Sistema PetShop 1.0")

menu = ["Login", "Cadastrar"]
escolha = st.sidebar.selectbox("Navegação", menu)

if escolha == "Cadastrar":
    CadastroUsuario()

elif escolha == "Login":
    st.subheader("Login de Usuário")
    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        # Lógica de validação no banco (pode estar no seu db.py)
        # Se válido:
        st.session_state['logado'] = True
        st.switch_page("exibir.py")