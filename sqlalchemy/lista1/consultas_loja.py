from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker as sessao
from modelos_loja import Produto
instrucao = select(Produto)
produto = sessao.query(Produto).get(0)
if produto:
     produto
else:
     'Nenhum produto encontrado!'
produto2 = sessao.execute(Produto).first()
print(f"Usando first \n {aluno2}")
produto3 = sessao.execute(Produto).scalars().all()
produto3_1 = produto3[0]
print(produto3_1)
produto4_2 = sessao.execute(select(Produto)).all()
produto4_3 = sessao.execute(select(Produto)).scalars().all()
print(f"Para buscar dados usamos o scalars() e all(), o all() retorna uma lista de tuplas para acessar o email de aluno teriamos que escrevre o seguinte comando 'aluno = sessao.execute(select(Aluno)).all()' que resultaria em: {produto}, com o método scalars ficaria 'aluno = sessao.execute(select(Aluno)).scalars().all() resultado em um objeto pode seracessados pela sua propiedade, Resultado: {produto4_3}")

produto_emestoque = sessao.query(Produto).filter_by(em_estoque=True)
print(f'Produtos em estoque: {produto_emestoque}')

##Filtro Avançado/Expressão: Use .filter() com expressões Python para encontrar produtos cujo preço seja maior que R$ 100,00 E cujo nome contenha a palavra 'Gamer' (use .like() ou .ilike()).
produto_filtrado = sessao.query(Produto).filter(Produto.preco > 10 and Produto.filter(Produto.nome.like('%Gamer')))
print(f'Produtos com preço maior que 100 e contendo "Gamer"  no nome: {produto_filtrado}')

# turma_existe = exists().where(Turma.turma_id=5)
categoria_existe= sessao.query(Categoria).filter(Categoria.exists() == True).all()
if categoria_existe:
    print('A categoria salvas na memória.')
else: 
    print("Não a categorias salvas.")
prodQuant = sessao.query(Produto).where(Produto.id == Produto.id).count()
print(f"A quantidade de produtos criados é {prodQuant}")
categorias_distintas = sessao.query(Categoria.nome).distinct().all()
print(f"As categorias distintas são: {categorias_distintas}")


tamanho_pag=5
pag_atual = 2

pag_prod =session.query(Produtos).order_by(Produto.preco.desc().limit(tamanho_pag).offset((pag_atual-1)*tamanho_pag)).all()
print(f'Segue abaixo a lista de produtos: \n {pag_prod}')

lista_produto = session.query(Produto).join(Categoria).all()
print(f"Segue a lista de produtos com as suas categorias \n {lista_produto}")

Lista_prod = session.query(Produto).outerjoin(Categoria).filter(Categoria.id == None).all()
print(f"Segue a lista de produtos sem categoria \n {Lista_prod}")

alunoTurma = session.query(Aluno).join(Turma)

#Agrupe os produtos por categoria_id utilizando .group_by().
prod_categoria = sessao.query(Produto).group_by(Produto.categoria_id).all()        
for produto in prod_categoria:
   print(f"Segue a lista de produtos: \n {produto}")

#Para cada grupo, calcule o preço médio dos produtos (func.avg(Produto.preco)) e o total de produtos estocados (func.count(Produto.id)).
preco_medio = sessao.query(Produto.categoria_id, func.avg(Produto.preco).label("preço_médio"), func.count(Produto.id).label("total_produtos")).group_by(Produto.categoria_id).order_by(Produto.categoria_id.asc()).all()

#Aplique um filtro pós-agrupamento com .having() para exibir apenas as categorias cujo preço médio dos produtos seja superior a R$ 250,00.

preco_acima = sessao.query(Produto.categoria_id, func.avg(Produto.preco).label("preço_médio"), func.count(Produto.id).label("total_produtos")).group_by(Produto.categoria_id).having(func.avg(Produto.preco > 250.00)).order_by(Produto.categoria_id.asc()).all()
print("--- CATEGORIAS COM MÉDIA ACIMA DE R$ 250,00 ---")
for categoria in preco_acima:
    print(f" Categoria: {categoria.categoria_id} - Preço médio maior que $250.00: {categoria.preço_médio} - Total de produtos: {categoria.total_produtos}")

produto_em_estoque = session.query(Produto).filter(Produto.em_estoque == True)
produto_em_black = produto_em_estoque.add_colums(produto_em_estoque.preco * 0.85).label("preco_promocional").all()
for produto, preco_promocional,produto_em_estoque.preco in produto_em_black:
    print(f"Produto: {produto.nome} - Preço promocional: {preco_promocional}, Preço original: {produto_em_estoque.preco}")
