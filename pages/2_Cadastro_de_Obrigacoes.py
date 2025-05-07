import streamlit as st
import pandas as pd
import datetime

# Configuração da página (deve ser o primeiro comando st)
st.set_page_config(page_title="Cadastro de Obrigações", layout="wide")

# Importações
from models import salvar_obrigacao, init_db
from utils.ui import aplicar_tema_leverage

# Aplica o tema
aplicar_tema_leverage()

# Título da página
st.title("📝 Cadastro de Obrigações via Planilha")

# Inicializa o banco de dados
init_db()

# Descrição da função
st.markdown("""
### Instruções
1. Faça o upload de uma planilha (.xlsx, .xls ou .csv) com os dados das obrigações
2. A planilha deve conter as colunas: **Operação**, **Gestora**, **Descrição**, **Categoria**, **Periodicidade**, **Data de Vencimento** e **Status**
3. Verifique se os dados estão corretos na prévia e confirme o cadastro
""")

# Upload de arquivo
uploaded_file = st.file_uploader("📁 Faça o upload da Planilha de Obrigações", type=["xlsx", "xls", "csv"])

if uploaded_file is not None:
    try:
        # Lê o arquivo
        if uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)
        
        # Verifica as colunas obrigatórias
        colunas_necessarias = ["Operação", "Gestora", "Descrição", "Categoria", "Periodicidade", "Data de Vencimento", "Status"]
        colunas_faltando = [col for col in colunas_necessarias if col not in df.columns]
        
        if colunas_faltando:
            st.error(f"❌ Faltam as seguintes colunas obrigatórias: {', '.join(colunas_faltando)}")
        else:
            # Formata a coluna de data
            try:
                if df["Data de Vencimento"].dtype != 'datetime64[ns]':
                    df["Data de Vencimento"] = pd.to_datetime(df["Data de Vencimento"])
            except Exception as e:
                st.warning(f"⚠️ Não foi possível converter a coluna 'Data de Vencimento' para o formato de data. Erro: {str(e)}")
            
            # Mostra prévia dos dados
            st.subheader("Prévia dos dados")
            st.dataframe(df)
            
            # Botão para confirmar cadastro
            if st.button("✅ Confirmar Cadastro", type="primary"):
                with st.spinner("Cadastrando obrigações..."):
                    # Contador de sucessos e falhas
                    sucessos = 0
                    falhas = 0
                    
                    # Progresso
                    progress_bar = st.progress(0)
                    total_rows = len(df)
                    
                    # Itera sobre as linhas do DataFrame
                    for i, row in df.iterrows():
                        try:
                            # Prepara os dados
                            obrigacao_data = {
                                "operacao": str(row["Operação"]),
                                "gestora": str(row["Gestora"]),
                                "descricao": str(row["Descrição"]),
                                "categoria": str(row["Categoria"]),
                                "periodicidade": str(row["Periodicidade"]),
                                "data_vencimento": row["Data de Vencimento"].date() if hasattr(row["Data de Vencimento"], 'date') else row["Data de Vencimento"],
                                "status": str(row["Status"]),
                            }
                            
                            # Opcionais
                            if "Ação" in df.columns and not pd.isna(row["Ação"]):
                                obrigacao_data["acao"] = str(row["Ação"])
                            
                            if "Notificação" in df.columns and not pd.isna(row["Notificação"]):
                                obrigacao_data["notificacao"] = str(row["Notificação"])
                            
                            if "Observações" in df.columns and not pd.isna(row["Observações"]):
                                obrigacao_data["observacoes"] = str(row["Observações"])
                            
                            # Salva no banco
                            salvar_obrigacao(obrigacao_data)
                            sucessos += 1
                        except Exception as e:
                            falhas += 1
                            st.error(f"Erro ao cadastrar a linha {i+1}: {str(e)}")
                        
                        # Atualiza a barra de progresso
                        progress_bar.progress((i + 1) / total_rows)
                    
                    # Resultado final
                    if sucessos > 0:
                        st.success(f"✅ {sucessos} obrigações cadastradas com sucesso!")
                    
                    if falhas > 0:
                        st.warning(f"⚠️ {falhas} obrigações não puderam ser cadastradas.")
    
    except Exception as e:
        st.error(f"❌ Erro ao processar o arquivo: {str(e)}")
