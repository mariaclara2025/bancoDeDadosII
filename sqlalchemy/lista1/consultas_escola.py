from sqlalchemy import create_engine, select,exists
from sqlalchemy.orm import sessionmaker as session
from modelos_escola import Aluno, Turma

instrucao = select(Aluno)
aluno = session.query(Aluno).get(1)
if aluno:
     print(aluno)
else:
    print('Nenhum produto encontrado!') 
aluno2 = session.execute(aluno).first()
print(f"Usando first \n {aluno2}")
aluno3 = session.execute(aluno).scalars().all()
aluno3_1 = aluno3[0]
print(aluno3_1)
aluno4_2 = session.execute(select(Aluno)).all()
aluno4_3 = session.execute(select(Aluno)).scalars().all()
print(f"Para buscar dados usamos o scalars() e all(), o all() retorna uma lista de tuplas para acessar o email de aluno teriamos que escrevre o seguinte comando 'aluno = sessao.execute(select(Aluno)).all()' que resultaria em: {aluno}, com o método scalars ficaria 'aluno = sessao.execute(select(Aluno)).scalars().all() resultado em um objeto pode seracessados pela sua propiedade, Resultado: {aluno4_3}")
session.execute(select(Aluno)).all()

#Filtro Simples: Use .filter_by() para encontrar a turma que possui o nome_turma='3º Ano A'.

turma_filtrada = session.query(Turma).filter_by(nome_turma = '3º Ano A' )
#Filtro Composto: Use .filter() com a cláusula lógica or_ do SQLAlchemy para buscar alunos nascidos após o ano de 2005 OU cujo e-mail pertença ao domínio '@escola.com' (utilize .endswith() ou like('%@escola.com')).
aluno_filtrada = session.query(Aluno).filter(data_nascimento = 2005 or Aluno.email.filter(Aluno.email.like('%@escola.com')))


turma_existe =session.query(Turma).where(Turma.turma_id=5).exists()
if turma_existe:
    print('A turma existe!')
else:
    print('A turma não existe!')

alunoQuant = session.query(Aluno).where(Aluno.id == Aluno.id).count()
print(f"A quantidade de alunos matriculados: \n {alunoQuant}")

alunoQuant = session.query(Aluno).order_by(Aluno.nome.asc())
print(f"A quantidade de alunos matriculados: \n {alunoQuant}")


tamanho_pag=10
pag_atual = 3

alunos = session.query(Aluno).order_by(Aluno.nome.asc().limit(tamanho_pag).offset((pag_atual-1)*tamanho_pag)).all()
print(f'Segue abaixo a lista de alunos: \n {alunos}')
#9.2 Agrupe os alunos por turma_id utilizando .group_by().
aluno_agrupados = session.query(Aluno).group_by(Aluno.turma_id).all()


#Calcule o número total de alunos por turma utilizando func.count(Aluno.id).
aluno_turma = session.query(Aluno).group_by(Aluno.turma_id).all()

#Calcule o número total de alunos por turma utilizando func.count(Aluno.id).
aluno_por_turma = session.query(Aluno.turma.id, func.count(Aluno.id)).group_by(Aluno.turma_id).all()

#Utilize a instrução .having() para filtrar e exibir no relatório apenas as turmas que possuem mais de 30 alunos matriculados

turma_30 = session.query(Aluno.turma_id, func.count(Aluno.id)).group_by(Aluno.turma_id).having(func.count(Aluno.id) > 30).all()

print("--- RELATÓRIO: TURMAS COM MAIS DE 30 ALUNOS MATRICULADOS ---")
for linha in relatorio_turmas:
    print(f"ID Turma: {linha.turma_id} | "
          f"Total de Alunos: {linha.total_alunos}")

#Questão 10.1 — Sistema: Loja Virtual

#Construa uma consulta base buscando alunos de determinada turma. Em seguida, utilizando o método .add_columns(), adicione uma projeção calculada ou campo informativo dinâmico (por exemplo, simulando a idade aproximada do aluno ou rotulando o status com base na data de nascimento).
aluno_turma = session.query(Aluno).filter(aluno.turma_id ==1).add_colums((func.date_part('year', func.now()) - func.date_part('year', Aluno.data_nascimento)).label("idade_aproximada")).all()
for aluno, idade_aproximada in aluno_turma:
    print(f"Aluno: {aluno.nome} - Idade aproximada: {idade_aproximada}")