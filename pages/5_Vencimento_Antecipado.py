from utils.ui import aplicar_tema_leverage
aplicar_tema_leverage()

import streamlit as st
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import pandas as pd

st.title("Vencimento Antecipado")

Base = declarative_base()
DB_PATH = "sqlite:///leverage.db"
engine = create_engine(DB_PATH)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

class VencimentoAntecipado(Base):
    __tablename__ = "vencimentos_antecipados"
    id = Column(Integer, primary_key=True)
    parte = Column(String)
    tipo_evento = Column(String)
    data_ocorrencia = Column(Date)
    status = Column(String)
    valor_maximo = Column(String)
    fonte = Column(String)
    acao_recomendada = Column(String)
    enviado_ao_juridico = Column(Boolean)
    data_cadastro = Column(Date)

Base.metadata.create_all(bind=engine)

st.markdown("### Nova Ocorrência Crítica")
with st.form("form_vencimento"):
    parte = st.text_input("Parte")
    tipo_evento = st.selectbox("Tipo de Evento", [
        "Eventos Societários", "Ações Judiciais", "Decisões Administrativas", "Falência/Recuperação",
        "Protestos", "Descumprimento Pecuniário", "Não Pecuniário", "Cross Default",
        "Licenças", "Constrições Judiciais", "Morte de partes", "Extinção de Contrato",
        "Transferência de Bens", "Problemas com Lastro", "Restrições de Crédito"
    ])
    data_ocorrencia = st.date_input("Data da Ocorrência", value=date.today())
    status = st.selectbox("Status", ["Em apuração", "Confirmado", "Não ocorreu"])
    valor_maximo = st.text_input("Valor Máximo Aplicável")
    fonte = st.text_input("Fonte da Informação")
    acao_recomendada = st.text_area("Ação Recomendada")
    enviado = st.checkbox("Notificar Jurídico", value=True)
    submit = st.form_submit_button("Salvar")

if submit:
    nova = VencimentoAntecipado(
        parte=parte,
        tipo_evento=tipo_evento,
        data_ocorrencia=data_ocorrencia,
        status=status,
        valor_maximo=valor_maximo,
        fonte=fonte,
        acao_recomendada=acao_recomendada,
        enviado_ao_juridico=enviado,
        data_cadastro=date.today()
    )
    db.add(nova)
    db.commit()
    st.success("Ocorrência registrada com sucesso!")

# Mostrar tabela
registros = db.query(VencimentoAntecipado).all()
if registros:
    dados = [{
        "Parte": r.parte,
        "Tipo": r.tipo_evento,
        "Data": r.data_ocorrencia,
        "Status": r.status,
        "Valor": r.valor_maximo,
        "Fonte": r.fonte,
        "Jurídico": "✅" if r.enviado_ao_juridico else "❌"
    } for r in registros]
    st.dataframe(pd.DataFrame(dados), use_container_width=True)
else:
    st.info("Nenhuma ocorrência registrada.")
