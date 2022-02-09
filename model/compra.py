from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from model.sqlalchemy_start import sqlalchemy_starter

Session, Base, engine = sqlalchemy_starter()


class Compra(Base):
    __tablename__ = 'compra'
    id = Column(Integer, primary_key=True)
    cartao_id = Column(Integer, ForeignKey('cartao.id'))
    titulo = Column('titulo', String(32))
    valor = Column('valor', Float)
    qtd_parcelas = Column('qtd_parcelas', Integer)
    data = Column('data', Date)
    cartao = relationship('Cartao')

    def __init__(self, cartao_id, titulo, valor, qtd_parcelas, data):
        self.cartao_id = cartao_id
        self.titulo = titulo
        self.valor = valor
        self.qtd_parcelas = qtd_parcelas
        self.data = data
