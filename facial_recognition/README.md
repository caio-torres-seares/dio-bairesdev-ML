# Reconhecimento Facial com DeepFace

Projeto desenvolvido como desafio para o bootcamp de Machine Learning da **BairesDev / Dio.me**.

O objetivo foi implementar em **Python** um sistema de **reconhecimento facial** capaz de identificar múltiplos rostos em uma imagem e compará-los com um **banco de dados local de faces**, utilizando a biblioteca **DeepFace**.

O projeto demonstra o fluxo completo de reconhecimento facial: detecção, extração, comparação e marcação das faces na imagem original.

## Etapas do Projeto

1. **Configuração do Ambiente**
   - Montagem do Google Drive.
   - Instalação das bibliotecas necessárias: `deepface` e `opencv-python`.

2. **Preparação dos Dados**
   - Definição do **banco de faces** (`faces_db`) contendo imagens de referência.
   - Definição da imagem de teste (`test_img_path`) que contém múltiplos rostos.
   - Mapeamento de nomes "bonitos" para os arquivos do banco (`messi`, `cr7`, `neymar`).

3. **Detecção de Rostos**
   - Utilização do detector **MTCNN** para localizar múltiplos rostos na imagem.
   - Extração de cada rosto individualmente para normalização.

4. **Reconhecimento**
   - Comparação de cada rosto detectado com o banco de faces usando o modelo **VGG-Face**.
   - Métrica utilizada: **cosine distance**.
   - Determinação do melhor match e conversão do nome do arquivo para uma exibição amigável.

5. **Visualização**
   - Adição de caixas ao redor dos rostos:
     - **Verde** → rosto reconhecido.
     - **Vermelho** → rosto desconhecido.
   - Exibição da imagem final com os nomes das pessoas sobre cada rosto.

## Tecnologias

- Python 3
- Google Colab
- **DeepFace** (detecção e reconhecimento facial)
- **OpenCV** (manipulação de imagens)
- **Matplotlib** (visualização de resultados)

