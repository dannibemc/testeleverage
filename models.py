from sqlalchemy import create_engine, Column, Integer, String, Date, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

DATABASE_URL = "sqlite:///db_obrigacoes.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Obrigacao(Base):
    __tablename__ = "obrigacoes"

    id = Column(Integer, primary_key=True, index=True)
    operacao = Column(String)
    gestora = Column(String)
    descricao = Column(Text)
    categoria = Column(String)
    periodicidade = Column(String)
    data_vencimento = Column(Date)
    status = Column(String)
    dias_para_vencimento = Column(Integer)
    acao = Column(Text)
    notificacao = Column(Text)
    ultima_cobranca = Column(Date)
    observacoes = Column(Text)

def init_db():
    Base.metadata.create_all(bind=engine)

def salvar_obrigacao(db_session, obrigacao_data):
    nova = Obrigacao(**obrigacao_data)
    db_session.add(nova)
    db_session.commit()

def atualizar_obrigacao(id, dados):
    session = SessionLocal()
    obrigacao = session.query(Obrigacao).filter_by(id=id).first()
    if obrigacao:
        for chave, valor in dados.items():
            setattr(obrigacao, chave, valor)
        session.commit()
        return True
    return False

def deletar_obrigacao(id):
    session = SessionLocal()
    obrigacao = session.query(Obrigacao).filter_by(id=id).first()
    if obrigacao:
        session.delete(obrigacao)
        session.commit()
        return True
    return False
