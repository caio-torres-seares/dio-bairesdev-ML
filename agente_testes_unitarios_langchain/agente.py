import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import argparse

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def gerar_testes(caminho_arquivo_python):
    """
    Função principal que lê um arquivo Python, envia para a IA
    e gera um arquivo de testes unitários com pytest.
    """
    # Verifica se o arquivo de entrada existe
    if not os.path.exists(caminho_arquivo_python):
        print(f"Erro: O arquivo '{caminho_arquivo_python}' não foi encontrado.")
        return

    # Lê o conteúdo do arquivo Python
    with open(caminho_arquivo_python, 'r', encoding='utf-8') as f:
        codigo_python = f.read()

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
    )

    # 2. Definição do Template do Prompt 
    template_string = """
    Você é um especialista em desenvolvimento de software e testes em Python.
    Sua tarefa é criar testes unitários usando a biblioteca pytest para o seguinte código Python.

    **Instruções:**
    1.  Crie um conjunto completo de testes unitários.
    2.  O arquivo de teste deve começar com `import pytest`.
    3.  Importe as funções necessárias do módulo original.
    4.  Crie testes para casos de sucesso (caminho feliz).
    5.  Crie testes para casos de falha e exceções (ex: entradas inválidas, divisão por zero, etc.).
    6.  As funções de teste devem seguir o padrão `def test_*`.
    7.  Retorne APENAS o código Python para o arquivo de teste. Não inclua explicações, comentários extras ou ```python.

    **Código Python para testar:**
    ```python
    {code}
    ```

    **Arquivo de Teste (somente o código):**
    """
    prompt_template = ChatPromptTemplate.from_template(template_string)

    # 3. Criação da "Chain" 
    chain = prompt_template | llm

    # 4. Invocação da Chain 
    resposta = chain.invoke({"code": codigo_python})

    # 5. Processamento e Salvamento do Resultado)
    codigo_teste = resposta.content
    nome_base = os.path.splitext(os.path.basename(caminho_arquivo_python))[0]
    nome_arquivo_teste = f"test_{nome_base}.py"

    with open(nome_arquivo_teste, 'w', encoding='utf-8') as f:
        f.write(codigo_teste)

    print(f"Arquivo de teste '{nome_arquivo_teste}' gerado com sucesso usando Google Gemini!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gera testes unitários para um arquivo Python usando Google Gemini.")
    parser.add_argument("arquivo", help="O caminho para o arquivo Python que será testado.")

    args = parser.parse_args()
    gerar_testes(args.arquivo)