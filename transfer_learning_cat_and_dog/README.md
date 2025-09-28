# Classificação de Imagens de Gatos e Cachorros 🐱🐶

Projeto desenvolvido no **Google Colab** para estudo de **Redes Neurais Convolucionais (CNNs)** e **Transfer Learning** com **Keras/TensorFlow**.  

O objetivo foi criar e treinar modelos de deep learning para classificar imagens entre **gatos** e **cachorros**, utilizando tanto uma CNN do zero quanto **transfer learning** com o modelo **VGG16** pré-treinado no ImageNet.

---

## 📂 Etapas do Projeto

1. **Montagem do Google Drive**  
   - Importação do dataset *Kaggle Cats and Dogs*.  
   - Organização em pastas locais no Colab.  

2. **Pré-processamento dos dados**  
   - Redimensionamento das imagens para `224x224`.  
   - Normalização dos pixels.  
   - Conversão dos rótulos para *one-hot encoding*.  
   - Divisão em **treino (70%)**, **validação (15%)** e **teste (15%)**.  

3. **Modelagem com CNN personalizada**  
   - Criação de uma rede convolucional com múltiplas camadas de `Conv2D`, `MaxPooling2D`, `Dropout` e `Dense`.  
   - Treinamento inicial com **10 épocas**.  

4. **Transfer Learning com VGG16**  
   - Uso do modelo **VGG16** com pesos pré-treinados no ImageNet.  
   - Camadas congeladas, mantendo apenas a última camada densa treinável.  
   - Treinamento adicional com **5 épocas**.  

5. **Avaliação**  
   - Métricas de **loss** e **accuracy** para treino, validação e teste.  
   - Comparação entre CNN do zero e Transfer Learning.  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**  
- **Google Colab**  
- **Keras / TensorFlow**  
- **NumPy / Matplotlib**  
- **Pillow (PIL)**  

---

## 📊 Resultados

- **CNN personalizada**:  
  - Acurácia de teste: ~66%  
- **Transfer Learning com VGG16**:  
  - Acurácia de teste: ~84%  

Os gráficos de *loss* e *accuracy* mostram claramente a melhora no desempenho com o uso de **transfer learning**.

---
