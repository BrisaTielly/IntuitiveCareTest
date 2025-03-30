from fastapi import FastAPI, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Busca de Operadoras")

origins = [
    "http://localhost:8000",  # URL do frontend local
    "http://intuitivecarefront.s3-website.us-east-2.amazonaws.com/",  # Endereço do frontend
]

#Configurações abertas para fins de facilitação de testes
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  
    allow_headers=["*"],  
)
 
#Caso queira rodar no seu servidor da aws, descomente a linha abaixo e comente a linha acima e configure a url no .env 
# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql://admin:admin@localhost/intuitive_care" #Vai rodar localmente

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

import re

@app.get("/search")
def search_operadoras(
    query: str = Query(..., description="Termo para busca"),
    maxResults: int = Query(10, le=50, ge=1, description="Número máximo de resultados"),
    db: Session = Depends(get_db)
):
    # A consulta utilizando ILIKE para buscar insensivelmente (maiúsculas e minúsculas)
    sql = text("""
        SELECT *
        FROM relatorio_cadop
        WHERE (razao_social ILIKE :q OR nome_fantasia ILIKE :q)
        LIMIT :maxResults
    """)
    
    # Passando a consulta com wildcards '%' para o ILIKE
    result = db.execute(sql, {"q": f"%{query}%", "maxResults": maxResults})
    registros = [dict(row._mapping) for row in result]
    
    # Retornar resposta com cabeçalhos CORS
    return JSONResponse(
        content={"results": registros},
        headers={
            "Access-Control-Allow-Origin": "*",  # Permite qualquer origem
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",  # Métodos permitidos
            "Access-Control-Allow-Headers": "*",  # Permite todos os cabeçalhos
        }
    )
