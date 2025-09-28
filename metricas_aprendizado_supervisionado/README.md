# Cálculo de Métricas de Avaliação de Aprendizado Supervisionado

Projeto desenvolvido como desafio para o bootcamp de Machine Learning da **BairesDev / Dio.me**.

O objetivo foi implementar em **Python**, a partir de funções manuais, um algoritmo para calcular as principais métricas de avaliação de um modelo de classificação:
- **Verdadeiro Positivo (VP)**, **Verdadeiro Negativo (VN)**, **Falso Positivo (FP)** e **Falso Negativo (FN)**.
- **Acurácia**, **Precisão**, **Sensibilidade (Recall)** e **F1-Score**.

A proposta é demonstrar um fluxo completo de Machine Learning (treino, teste e avaliação), mas com foco no cálculo "do zero" das métricas, sem utilizar as funções prontas como `confusion_matrix` ou `classification_report` do Scikit-learn para a contagem e o cálculo, reforçando o entendimento teórico por trás de cada uma.

## Etapas do Projeto
1.  **Carregamento e Preparação dos Dados**:
    - O dataset **Wine** (`load_wine`) do Scikit-learn é carregado.
    - O problema, originalmente multiclasse (3 tipos de vinho), é convertido para uma **classificação binária** para simplificar a análise (vinho "Classe 0" vs. "Não Classe 0").
2.  **Treinamento do Modelo**:
    - Os dados são divididos em conjuntos de treino (80%) e teste (20%).
    - Um modelo de **Regressão Logística** é treinado com os dados de treino.
3.  **Cálculo Manual das Métricas**:
    - O modelo treinado faz previsões no conjunto de teste.
    - Uma função customizada (`calcular_metricas`) itera sobre os resultados, comparando os valores reais com os previstos para contar manualmente os VPs, VNs, FPs e FNs.
    - Com base nesses contadores, a mesma função calcula a acurácia, precisão, sensibilidade e o F1-Score.
4.  **Exibição dos Resultados**:
    - Os valores contados e as métricas calculadas são impressos no console.
    - Uma **matriz de confusão** é gerada com os resultados e plotada usando Matplotlib/Seaborn para uma visualização clara do desempenho.

## Tecnologias
- Python 3
- Google Colab
- **Scikit-learn** (apenas para carregar o dataset, dividir os dados e treinar o modelo)
- **NumPy**
- **Matplotlib** e **Seaborn** (para visualização da matriz de confusão)

## Resultados
O notebook executa o fluxo completo e gera duas saídas principais:
- **Relatório de texto** com a contagem de VP, VN, FP, FN e os valores calculados para cada métrica de avaliação.
- **Gráfico da Matriz de Confusão**, que exibe visualmente os acertos e erros do modelo.
