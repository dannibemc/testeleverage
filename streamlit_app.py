import streamlit as st
import base64
import os

st.set_page_config(page_title="Leverage", layout="wide")

st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #FFFFFF;
            color: #343E83;
            font-family: 'Montserrat', sans-serif;
        }
        h1, h2, h3 {
            font-family: 'Comfortaa', cursive;
            color: #343E83;
        }
        .css-18e3th9 {
            background-color: #F8F9FA;
        }
        .logo-container {
            position: absolute;
            top: 15px;
            right: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

logo_path = "leverage_logo.png"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"<div class='logo-container'><img src='data:image/png;base64,{encoded}' height='90'></div>",
        unsafe_allow_html=True
    )

st.sidebar.header("📚 Navegação")
page = st.sidebar.radio("Ir para:", [
    "Dashboard",
    "Upload Inteligente",
    "Mapeamento de Obrigações",
    "Cadastro de Obrigações",
    "Monitoramento de Crédito",
    "Vencimento Antecipado",
    "Due Diligence",
    "Administração"
])

st.title("Leverage - Plataforma de Gestão de Obrigações")

st.info(f"Você está visualizando a página: {page}")
