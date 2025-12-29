import streamlit as st
from banco.tabela import criar_tabelas
from funções.cadastroUsuario import CadastroUsuario

# 1. Inicializa o banco de dados logo de cara
criar_tabelas()

# 2. Define a função de login
def tela_login():
    st.title("🐾 Sistema PetShop 1.0")
    aba1, aba2 = st.tabs(["Acessar Conta", "Novo Cadastro"])
    
    with aba1:
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            # Aqui você deve colocar a validação real do banco depois
            # Por enquanto, vamos simular o sucesso:
            st.session_state['logado'] = True
            st.session_state['usuario_atual'] = [1, "Usuário Teste", 30, "000", "123", "123", "Rua X", email, senha, None]
            st.rerun() 
            
    with aba2:
        CadastroUsuario()

# LÓGICA DE EXECUÇÃO 

# Garante que a variável 'logado' existe na memória
if 'logado' not in st.session_state:
    st.session_state['logado'] = False

# Se NÃO estiver logado, CHAMA a função de login
if not st.session_state['logado']:
    tela_login()
else:
    # Se JÁ estiver logado, redireciona automaticamente para a página de exibição
    st.switch_page("pages/1_exibir.py")