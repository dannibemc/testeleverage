import streamlit as st

def aplicar_tema_leverage():
    """
    Aplica o tema visual padrão do Leverage Securitizadora.
    """
    st.markdown("""
    <style>
    .main-header {
        color: #1E3A8A;
        font-size: 24px;
        font-weight: bold;
    }
    .sub-header {
        color: #334155;
        font-size: 18px;
        font-weight: 600;
    }
    .card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .status-pendente {
        color: #f59e0b;
        font-weight: bold;
    }
    .status-concluido {
        color: #10b981;
        font-weight: bold;
    }
    .status-atrasado {
        color: #ef4444;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)