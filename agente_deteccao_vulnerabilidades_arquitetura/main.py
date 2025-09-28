from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from typing import Annotated
import uvicorn
from analysis_service import analyze_with_gemini

AI_ANALYSIS_FUNCTION = analyze_with_gemini


app = FastAPI(
    title="API de Análise de Ameaças STRIDE com IA",
    description="Faça upload de um diagrama de arquitetura e receba uma análise de ameaças STRIDE.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Análise de Ameaças STRIDE."}

@app.post("/analyze/stride")
async def analyze_architecture(file: UploadFile = File(...)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Formato de arquivo inválido. Por favor, envie uma imagem.")

    try:
        # Lê o conteúdo da imagem em bytes
        image_bytes = await file.read()

        # Chama a função de análise da IA
        analysis_result = AI_ANALYSIS_FUNCTION(image_bytes)

        # Retorna o resultado
        return {
            "filename": file.filename,
            "analysis": analysis_result
        }
    except Exception as e:
        # Em caso de erro na chamada da API da IA ou outro problema
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro ao processar a imagem: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)