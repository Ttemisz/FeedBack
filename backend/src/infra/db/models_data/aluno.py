from sqlalchemy import Column, Integer, String, Float, ForeignKey
from infra.db.settings.base import Base

class Aluno(Base):
    """
    Tabela que armazena os dados dos alunos.

    Atributos:
        id (int): Identificador único do aluno.
        nome (str): Nome completo do aluno.
        cpf (str): CPF do aluno.
        idade (int): Idade do aluno.
        faltas (int): Número de faltas do aluno.
        nota_score_preditivo (float): Score preditivo de desempenho do aluno.
        id_escola (int): Chave estrangeira para a tabela Escola.
        id_turma (int): Chave estrangeira para a tabela Turma.
        id_responsavel (int): Chave estrangeira para a tabela Responsavel.
    """
    __tablename__ = "aluno"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    faltas = Column(Integer, default=0, nullable=False)
    nota_score_preditivo = Column(Float, nullable=True) # Pode ser nulo no início
    id_escola = Column(Integer, ForeignKey('escola.id'), nullable=False)
    id_turma = Column(Integer, ForeignKey('turma.id'), nullable=False)
    id_responsavel = Column(Integer, ForeignKey('responsavel.id'), nullable=False)

    def __repr__(self) -> str:
        return f"<Aluno id={self.id}, nome='{self.nome}'>"
