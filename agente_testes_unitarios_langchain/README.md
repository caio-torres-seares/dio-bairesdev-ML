# Agente de IA Gerador de Testes Unitários com LangChain e Google Gemini

## 📝 Descrição do Projeto

Este projeto é a resolução do desafio "Criando um Agente de IA com LangChain para Gerar Testes Unitários" da plataforma DIO (Digital Innovation One). O objetivo é construir um agente de Inteligência Artificial capaz de gerar automaticamente testes unitários em Python, utilizando a biblioteca `pytest`.

A implementação utiliza o framework **LangChain** para orquestrar a lógica e se conecta à poderosa **API do Google Gemini (via Google AI Studio)** para a geração do código. A solução foi adaptada para usar a API do Gemini como uma alternativa acessível e de alta performance em relação à proposta original com Azure OpenAI, demonstrando flexibilidade e o uso de tecnologias de ponta.

O agente recebe um arquivo Python como entrada e gera um arquivo de testes (`test_*.py`) correspondente, pronto para ser executado.

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o agente em sua máquina local.

### Pré-requisitos

-   Python 3.8 ou superior
-   Uma chave de API do Google Gemini. Você pode obter uma gratuitamente no [Google AI Studio](https://aistudio.google.com/).

### 1. Clonar o Repositório

```bash
git clone https://github.com/caio-torres-seares/agente-testes-unitarios-langchain.git
cd agente-testes-unitarios-langchain
```

### 2. Criar e Ativar o Ambiente Virtual

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Criar o ambiente
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate

# Ativar no Linux/Mac
source venv/bin/activate
```

### 3. Instalar as Dependências

As bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Instale-as com o seguinte comando:

```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente

Para que o agente possa se autenticar na API do Google, você precisa configurar sua chave secreta.

1.  Renomeie o arquivo `.env.example` para `.env`.
2.  Abra o arquivo `.env` e cole a sua chave de API do Google Gemini.

**Conteúdo do arquivo `.env`:**
```env
# Variável de ambiente para a API do Google Gemini
GOOGLE_API_KEY="COLE_SUA_CHAVE_DE_API_AQUI"
```

### 5. Executar o Agente para Gerar os Testes

Com tudo configurado, execute o script `agente.py`, passando como argumento o arquivo Python para o qual você deseja gerar os testes.

```bash
python agente.py funcoes.py
```

Após a execução, um novo arquivo chamado `test_funcoes.py` será criado no diretório.

### 6. Rodar os Testes Gerados

Finalmente, use o `pytest` para executar os testes que a IA criou e verificar se o código original está funcionando como esperado.

```bash
pytest
```

A saída no terminal indicará se todos os testes passaram com sucesso.

## 🛠️ Tecnologias Utilizadas

-   **Python**: Linguagem de programação principal.
-   **Google Gemini API**: Modelo de linguagem de última geração utilizado para a geração do código de teste.
-   **LangChain**: Framework para o desenvolvimento de aplicações com LLMs, usado para estruturar o prompt e a comunicação com a API.
-   **Pytest**: Framework para a escrita e execução dos testes unitários em Python.
-   **Python-Dotenv**: Biblioteca para gerenciamento de variáveis de ambiente.
