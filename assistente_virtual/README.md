# Assistente Virtual em Python

Projeto desenvolvido como desafio para o bootcamp de Machine Learning da **BairesDev / Dio.me**.

O objetivo foi criar um **assistente virtual** capaz de interagir com o usuário por **voz** ou **texto**, realizar pesquisas na Wikipedia, abrir sites e fornecer informações contextuais, utilizando **Python** e bibliotecas de processamento de áudio e fala.

O projeto demonstra um fluxo completo de interação: detecção de microfone, síntese de voz, reconhecimento de fala e execução de comandos.

## Funcionalidades

- **Modo voz**: o assistente fala e ouve comandos do usuário (usando microfone).
- **Modo texto**: caso não haja microfone, o assistente interage via terminal.
- **Comandos disponíveis**:
  - `pesquise por [termo]` → busca na Wikipedia e retorna um resumo.
  - `abrir o youtube` → abre o YouTube no navegador.
  - `procure no youtube por [termo]` → busca vídeos no YouTube.
  - `farmácia mais próxima` → abre o Google Maps mostrando farmácias próximas.
  - `encerrar` ou `parar` → finaliza a execução do assistente.

## Tecnologias

- Python 3
- Google Colab
- **gTTS** → conversão de texto em fala.
- **SpeechRecognition** → reconhecimento de voz via microfone.
- **playsound** → reprodução de áudio.
- **OpenCV** (opcional, para visualizações futuras).
