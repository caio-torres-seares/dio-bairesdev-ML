# Conversão de Imagens – Colorida → Escala de Cinza → Binarizada  

Projeto desenvolvido como parte do **curso de Machine Learning da DIO**.  

O objetivo foi implementar em **Python** um algoritmo simples para:  
- Converter uma imagem colorida para **níveis de cinza** (0–255).  
- Converter a imagem em cinza para uma versão **binarizada** (preto e branco, 0 ou 255).  

A proposta segue o exemplo de **binarização** visto em aula, mas sem utilizar bibliotecas específicas de visão computacional como OpenCV. O processamento é feito a partir do formato **PPM/PGM (Portable Pixmap/Grayscale)**, manipulando os valores de pixels diretamente em Python puro.  

## Etapas do Projeto
1. **Upload da imagem (PNG/JPG) no Google Colab**.  
2. Conversão para **PPM (P3 ASCII)** para facilitar a leitura em Python.  
3. Implementação das funções de:  
   - Leitura e escrita de imagens PPM/PGM.  
   - Conversão de RGB → Cinza usando a fórmula:  
     ```
     gray = 0.299*R + 0.587*G + 0.114*B
     ```  
   - Binarização a partir de um **limiar fixo (threshold = 128)**.  
4. Exibição dos resultados (colorida, cinza e binária) lado a lado.  

## Tecnologias
- Python 3  
- Google Colab  
- Matplotlib (apenas para exibição)  
- Pillow (apenas para conversão inicial de PNG → PPM)  

## Resultados
O notebook gera três versões da imagem:  
- **Original (colorida)**  
- **Escala de Cinza (0–255)**  
- **Binarizada (0 e 255, preto e branco)**  
