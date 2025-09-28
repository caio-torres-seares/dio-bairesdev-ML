# Detecção de Objetos com YOLOv8

Projeto desenvolvido como desafio para o bootcamp de Machine Learning da **BairesDev / Dio.me**.

O objetivo foi implementar em **Python** um pipeline completo de **detecção de objetos** utilizando o modelo pré-treinado **YOLOv8**, incluindo:

- Download e preparação de um subconjunto do dataset **COCO**.
- Criação de labels no formato YOLO a partir das anotações COCO.
- Treinamento de um modelo YOLOv8 customizado para detectar as classes **dog** e **car**.
- Validação do modelo com métricas como **mAP50** e **mAP50-95**.

## Etapas do Projeto

1. **Configuração do Ambiente**
   - Montagem do Google Drive.
   - Instalação das bibliotecas necessárias (`ultralytics`, `pycocotools`).
   - Clonagem e compilação do **Darknet** para suporte a GPU e OpenCV.

2. **Preparação do Dataset**
   - Download das anotações COCO.
   - Filtragem das categorias **dog** e **car**.
   - Seleção de 200 imagens e divisão em treino (80%) e validação (20%).
   - Criação das labels YOLO correspondentes às bounding boxes.
   - Geração do arquivo `dataset.yaml` para configurar o dataset no YOLO.

3. **Treinamento do Modelo**
   - Utilização do modelo **YOLOv8n** pré-treinado.
   - Treinamento com 100 épocas, batch size 16 e imagens redimensionadas para 640x640.
   - Salvamento de checkpoints e geração de gráficos de desempenho.

4. **Validação**
   - Avaliação do modelo treinado utilizando métricas como:
     - **mAP50**
     - **mAP50-95**
     - **Precisão** e **Recall** por classe.
   - Exibição de métricas detalhadas e gerais.

## Tecnologias

- Python 3
- Google Colab
- **Ultralytics YOLOv8**
- **PyTorch**
- **pycocotools**
- **Matplotlib**
- **NumPy**
- **Scikit-learn** (para dividir treino/validação)
- **Darknet** (compilado com suporte a GPU e OpenCV)
