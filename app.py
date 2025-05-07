import streamlit as st
from models import init_db
from utils.ui import aplicar_tema_leverage

# Configura a página
st.set_page_config(
    page_title="Leverage Obrigações",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Aplica o tema
aplicar_tema_leverage()

# Inicializa o banco de dados
init_db()

# Título e descrição
st.title("Leverage Obrigações")
st.subheader("Sistema de Gerenciamento de Obrigações")

# Informações da página inicial
st.markdown("""
### Bem-vindo ao Sistema de Gerenciamento de Obrigações da Leverage

Este sistema permite:
- Visualizar um dashboard com informações sobre obrigações
- Cadastrar novas obrigações via planilha
- Listar e filtrar todas as obrigações cadastradas
- Mapear obrigações através de documentos utilizando IA

Utilize o menu lateral para navegar entre as funcionalidades.
""")

# Estatísticas na página inicial (você pode personalizar)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total de Obrigações", value="--")

with col2:
    st.metric(label="Obrigações Pendentes", value="--")

with col3:
    st.metric(label="Vencendo esta Semana", value="--")
