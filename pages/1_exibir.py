# importa as funções e sintaxes do streamlit.
import streamlit as st

if 'logado' not in st.session_state or not st.session_state['logado']:
    st.warning("Por favor, faça login para acessar esta página.")
    st.stop()

