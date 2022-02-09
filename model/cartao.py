from sqlalchemy import Column, Integer, String, Float

from model.sqlalchemy_start import sqlalchemy_starter

Session, Base, engine = sqlalchemy_starter()


class Cartao(Base):
    __tablename__ = 'cartao'
    id = Column(Integer, primary_key=True)
    nome = Column('nome', String(32))
    vencimento = Column('vencimento', Integer)
    limite = ('limite', Float)

    def __init__(self, nome, vencimento, limite):
        self.nome = nome
        self.vencimento = vencimento
        self.limite = limite
