import streamlit as st
from funções.cadastroUsuario import CadastroUsuario

def tela_login():
    st.title("🐾 Sistema PetShop 1.0")
    aba1, aba2 = st.tabs(["Acessar Conta", "Novo Cadastro"])
    
    with aba1:
        # Aqui vai seu código de st.text_input de email e senha...
        if st.button("Entrar"):
            # Se validou no banco:
            st.session_state['logado'] = True
            st.rerun() # Isso faz o streamlit_app.py rodar de novo e te mandar pro exibir.py
            
    with aba2:
        CadastroUsuario()