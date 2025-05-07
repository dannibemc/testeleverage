import streamlit as st
import pandas as pd
import schedule
import time
import threading
from datetime import date, datetime
from models import get_all_obrigacoes  # Certifique-se de ter essa função
from utils.email_utils import enviar_email_cobranca  # Você criará este módulo

st.set_page_config(page_title="Lista de Obrigações", layout="wide")
st.title("📋 Lista de Obrigações Registradas")

# 1. Carrega obrigações
df = get_all_obrigacoes()
st.dataframe(df)

# 2. Botão de disparo manual
if st.button("📧 Disparar lembretes manualmente"):
    hoje = date.today().strftime("%Y-%m-%d")
    obrigacoes_hoje = df[df["data_vencimento"] == hoje]
    if obrigacoes_hoje.empty:
        st.warning("Nenhuma obrigação com vencimento hoje.")
    else:
        for _, row in obrigacoes_hoje.iterrows():
            enviar_email_cobranca(row)
        st.success(f"{len(obrigacoes_hoje)} lembretes enviados com sucesso.")

# 3. Agendador background (executa uma vez ao dia)
def rotina_diaria():
    hoje = date.today().strftime("%Y-%m-%d")
    obrigacoes_hoje = df[df["data_vencimento"] == hoje]
    for _, row in obrigacoes_hoje.iterrows():
        enviar_email_cobranca(row)
    print(f"[{datetime.now()}] Disparo automático feito.")

# Configura agendamento
schedule.every().day.at("08:00").do(rotina_diaria)

# Executa em background
def agendador_thread():
    while True:
        schedule.run_pending()
        time.sleep(60)

threading.Thread(target=agendador_thread, daemon=True).start()