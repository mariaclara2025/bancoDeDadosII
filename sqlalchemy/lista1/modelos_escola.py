from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey
Base = declarative_base()

class Aluno(Base):
    __tablename__="alunos"
    id = Column(Integer, primary_key=True)
    matricula = Column(String(20), unique=True, nullable=False )
    nome = Column(String(100), nullable=False)
    email = Column(String(120), unique=True,index=True)
    data_nascimento = Column(Date)
    turma_id = Column(ForeignKey('turmas.id'), nullable=True)
    def __repr__(self):
        return f'Aluno: {self.nome}, Matricula: {self.matricula}' 
class Turma(Base):
    __tablename__="turmas"
    id = Column(Integer, primary_key=True)
    nome_turma = Column(String(50), nullable=False)
    ano_letivo = Column(Integer, nullable=False)