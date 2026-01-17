from fastapi import FastAPI

app = FastAPI(title="Minha API na Nuvem", description="API desenvolvida para o desafio de Deploy no Azure")

@app.get("/")
def home():
    return {
        "mensagem": "API Online com Sucesso!",
        "plataforma": "Azure App Service",
        "tecnologia": "FastAPI & Python"
    }

@app.get("/status")
def check_status():
    return {"status": "operacional", "deploy": "concluido"}