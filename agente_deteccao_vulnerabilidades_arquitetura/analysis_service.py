import os
import base64
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

def analyze_with_gemini(image_bytes: bytes) -> str:
    """
    Envia a imagem para o Google Gemini Vision e retorna a análise STRIDE.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    prompt_text = """
    Você é um especialista em segurança da informação e arquitetura de aplicações.
    Sua tarefa é realizar uma análise de ameaças detalhada no diagrama de arquitetura fornecido na imagem.
    Utilize a metodologia STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) como base para a sua análise.

    Para cada categoria do STRIDE, identifique ameaças potenciais, vulnerabilidades e sugira possíveis mitigações.
    Se uma categoria não for aplicável, justifique brevemente.

    Formate a resposta em Markdown, com um cabeçalho para cada categoria do STRIDE.
    Exemplo de formato:

    ## Spoofing (Falsificação de Identidade)
    - **Ameaça:** Um atacante pode se passar por [componente X]...
    - **Mitigação:** Implementar [solução Y]...

    ## Tampering (Adulteração)
    - ...
    """
    
    message = HumanMessage(
        content=[
            {"type": "text", "text": prompt_text},
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64.b64encode(image_bytes).decode('utf-8')}"},
        ]
    )

    response = llm.invoke([message])
    return response.content