# Sistema de Recomendação de Imagens com Transfer Learning

Projeto desenvolvido como desafio para o bootcamp de **Machine Learning da BairesDev / Dio.me**.

O objetivo foi implementar, em **Python no Google Colab**, um sistema de recomendação de produtos baseado em imagens, utilizando **redes neurais pré-treinadas** para extrair embeddings visuais e comparar a similaridade entre imagens.  

Além disso, foi feito um modelo de **classificação de produtos** via *transfer learning*, que auxilia o sistema a recomendar itens da mesma categoria e com maior proximidade visual.

---

## Etapas do Projeto

1. **Organização e Aumento do Dataset**
   - Criação de diretórios para diferentes categorias de produtos (ex.: bicicleta, mouse, relógio, teclado).
   - Aplicação de **data augmentation** para aumentar a variabilidade do dataset usando `ImageDataGenerator` (rotações, zoom, flips).

2. **Extração de Embeddings com EfficientNetB0**
   - Uso da rede **EfficientNetB0** pré-treinada no ImageNet.
   - Cada imagem foi processada para gerar um vetor de **1280 dimensões** representando suas características visuais.
   - Os embeddings foram salvos em `.npy` e os caminhos das imagens em `.json`.

3. **Cálculo de Similaridade**
   - Implementação da métrica de **cosine similarity** para medir a proximidade entre imagens.
   - Construção de uma função de recomendação que exibe os itens mais semelhantes ao produto consultado.

4. **Treinamento de um Classificador com Transfer Learning**
   - A base **EfficientNetB0** foi congelada e utilizada como extrator de features.
   - Camadas adicionais de **GlobalAveragePooling + Dense Softmax** foram adicionadas.
   - O modelo foi treinado para classificar produtos em suas respectivas categorias.

5. **Sistema de Recomendação Híbrido**
   - Primeiro, o modelo classifica a imagem enviada.
   - Em seguida, recomenda apenas produtos **da mesma categoria**, ordenados pela **similaridade visual**.

---

## Tecnologias Utilizadas

- Python 3  
- Google Colab  
- **TensorFlow / Keras** (EfficientNetB0, treinamento e transfer learning)  
- **Scikit-learn** (cálculo de similaridade)  
- **NumPy** e **Pillow** (manipulação de dados e imagens)  
- **Matplotlib** (visualização das recomendações)  

---

## Resultados

O notebook executa um fluxo completo de **classificação e recomendação baseada em imagens**, gerando duas saídas principais:

As imagens retornadas correspondem a itens mais parecidos com a consulta, filtrados pela classe prevista pelo modelo.

---
