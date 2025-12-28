# importação de funçoes do streamlit
import streamlit as st

# garante que usuários não acessem as páginas por meio de URL
if 'logado' not in st.session_state or not st.session_state['logado']:
    st.warning("Por favor, faça login para acessar esta página.")
    st.stop() 
# Interrompe a renderização da página
# opções de excluir e atualizar dados já encapsuladas nesse arquivo.
