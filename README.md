# Analise e Tratamento de Pedidos (pedidos.py)

Este projeto consiste em um script em Python desenvolvido para realizar a leitura, limpeza, tratamento e consolidação de dados de vendas a partir de um arquivo CSV de pedidos.

O foco principal do projeto e aplicar regras de negocio, isolar outliers (anomalias de dados) e garantir a precisao do faturamento total.

---

## Funcionalidades

- Tratamento de Dados: Filtra registros incompletos ou com erro de formatacao.
- Deteccao Automatica de Outliers: Utiliza uma heuristica baseada na media (5x a media) para identificar volumes de compra atipicos (ex: erros de digitacao como 9.999 unidades).
- Relatorio de Faturamento: Calcula o faturamento consolidado considerando exclusivamente os pedidos validos, impedindo que anomalias distorcam os resultados financeiros.
- Metricas de Vendas: Identifica o produto mais vendido e consolida o volume por item.

---

## Tecnologias e Conceitos Aplicados

- Python 3 (Manipulacao de arquivos, dicionarios, listas e estruturas de repeticao)
- Engenharia e Analise de Dados: Limpeza de dados (Data Cleaning) e Tratamento de Excecoes/Outliers
- Regra de Negocio: Separacao de dados operacionais normais vs. auditoria de fraude ou erros

---

## Resultados Gerados

Ao executar o script sobre a base de testes:
1. Faturamento Total Valido: R$ 9.169,10
2. Produto Mais Vendido: Leite 1L (28 unidades)
3. Outliers Isolados: Pedido #1021 (Felipe Castro - 9.999 unidades) isolado com sucesso para auditoria sem impactar o faturamento.
