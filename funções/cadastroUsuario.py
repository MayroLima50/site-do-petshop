import streamlit as st
import sqlite3
import os

def CadastroUsuario():
    st.subheader("Realize seu cadastro preenchendo o formulário abaixo:")
    
    # Temos aqui o formulário, assim a página recarregará a cada clique.
    with st.form("form_cadastro", clear_on_submit=True):
        # informações básicas do usuário:
        nome = st.text_input("Digite seu nome:")
        idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, step=1)
        cpf = st.text_input("Digite seu CPF:")

        # bloco dos contatos e endereço dos usuários:
        contato1 = st.text_input("Digite seu telefone:")
        contato2 = st.text_input("Digite seu telefone alternativo:")
        end = st.text_input("Digite seu endereço:")

        # informações de login, senha e e-mail:
        email = st.text_input("Digite seu e-mail:")
        senha = st.text_input("Crie uma senha:", type="password")
        
        # Onde o usuário fará o Upload da Imagem que será usada como foto de indentificação.
        foto_perfil = st.file_uploader("Escolha uma imagem para usar como foto de identificação", type=['png', 'jpg', 'jpeg'])
        enviar = st.form_submit_button("Finalizar Cadastro")

        if enviar:
            if foto_perfil is not None:
                # 1. Salvar a imagem fisicamente
                if not os.path.exists("fotos_usuarios"):
                    os.makedirs("fotos_usuarios")
                
                caminho_foto = f"fotos_usuarios/{cpf}_{foto_perfil.name}"
                with open(caminho_foto, "wb") as f:
                    f.write(foto_perfil.getbuffer())
                
                # 2. Salvando no Banco de Dados
                try:
                    conn = sqlite3.connect('banco/petshop.db')
                    cursor = conn.cursor()
                    cursor.execute('''
                        INSERT INTO usuarios (nome, idade, cpf, contato1, contato2, endereco, email, senha, foto_path)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (nome, idade, cpf, contato1, contato2, end, email, senha, caminho_foto))
                    conn.commit()
                    conn.close()
                    st.success("Cadastrado com sucesso! Vá para a aba de Login.")
                except Exception as e:
                    st.error(f"Erro ao salvar no banco: {e}")
            else:
                st.warning("Por favor, insira uma foto de identificação.")