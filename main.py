
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

# String de conexão MongoDB (substituir pelos seus dados)
client = MongoClient("mongodb+srv://gracymmedeiros:t07OXnWH4ZjvUFTc@cluster0.om1cghm.mongodb.net/?retryWrites=true&w=majority")

# Conectando ao banco e coleção
db = client["meubanco"]
colecao = db["clientes"]

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    dados = list(colecao.find({}, {"_id": 0}))  # Ignorando o campo _id
    return templates.TemplateResponse("tabela.html", {"request": request, "dados": dados})
