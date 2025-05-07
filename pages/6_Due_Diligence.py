from utils.ui import aplicar_tema_leverage
aplicar_tema_leverage()

import streamlit as st
from datetime import date
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import pandas as pd

st.title("Due Diligence")

Base = declarative_base()
DB_PATH = "sqlite:///leverage.db"
engine = create_engine(DB_PATH)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

class DocumentoDiligencia(Base):
    __tablename__ = "documentos_diligencia"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    tipo = Column(String)
    data_recebimento = Column(Date)
    status = Column(String)

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

st.markdown("### Adicionar Documento de Due Diligence")
with st.form("form_doc"):
    nome = st.text_input("Nome do Documento")
    tipo = st.selectbox("Tipo", ["Estatuto", "Contrato Social", "Protesto", "Certidão", "Decisão Judicial", "Outro"])
    data_recebimento = st.date_input("Data de Recebimento", value=date.today())
    status = st.selectbox("Status", ["Pendente", "Recebido", "Análise"])
    submit = st.form_submit_button("Salvar")

if submit:
    novo = DocumentoDiligencia(nome=nome, tipo=tipo, data_recebimento=data_recebimento, status=status)
    db.add(novo)
    db.commit()
    st.success("Documento registrado!")

st.markdown("### Documentos Registrados")
docs = db.query(DocumentoDiligencia).all()
if docs:
    for d in docs:
        st.write(f"📄 {d.nome} | {d.tipo} | {d.status}")
        if st.button(f"⚠️ Criar Evento de Vencimento (Doc ID {d.id})", key=f"doc-{d.id}"):
            novo_evento = VencimentoAntecipado(
                parte="Devedora",
                tipo_evento="Ações Judiciais" if "judicial" in d.tipo.lower() else "Documentação",
                data_ocorrencia=d.data_recebimento,
                status="Em apuração",
                valor_maximo="",
                fonte=f"Doc. Due Diligence: {d.nome}",
                acao_recomendada="Avaliar impacto e acionar jurídico",
                enviado_ao_juridico=True,
                data_cadastro=date.today()
            )
            db.add(novo_evento)
            db.commit()
            st.success("Evento de Vencimento Antecipado criado com base no documento.")
else:
    st.info("Nenhum documento registrado.")
