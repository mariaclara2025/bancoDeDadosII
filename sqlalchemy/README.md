# Banco de Dados II — Persistência e Consultas Avançadas com SQLAlchemy

Este repositório contém a resolução de exercícios práticos da disciplina de **Banco de Dados II**. O objetivo principal das atividades é aplicar conceitos avançados de manipulação de dados, agregações e projeções dinâmicas utilizando o ORM **SQLAlchemy** em Python.

## 🛠️ Tecnologias e Conceitos Aplicados

* **SQLAlchemy ORM**: Mapeamento de entidades, gerenciamento de sessões (`Session`) e construção de queries programáticas.
* **Agregações e Agrupamentos**: Uso de `func.avg()`, `func.count()` e cláusulas `.group_by()` para consolidação de dados por categorias.
* **Filtros Avançados pós-agrupamento**: Aplicação do método `.having()` para validação de condições em dados agregados (substituindo o uso do `WHERE` tradicional quando aplicável).
* **Projeções Dinâmicas**: Utilização do método `.add_columns()` para injetar campos calculados em tempo de execução (como cálculos de descontos e extração de intervalos de datas com `func.extract`), permitindo a manipulação de resultados em formato de tuplas estruturadas.

## 📁 Estrutura dos Exercícios

As resoluções cobrem cenários do mundo real distribuídos em sistemas práticos:
1. **Sistema de Loja Virtual (E-commerce)**: Consultas de produtos, cálculo de ticket/preço médio por categoria e geração de preços promocionais dinâmicos para eventos (Black Friday).
2. **Sistema Escolar/Acadêmico**: Relatórios de matrículas por turmas com filtros de volumetria de alunos e projeções de dados cadastrais (como cálculo de idade aproximada).
