from fastapi import FastAPI, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Busca de Operadoras")

origins = [
    "http://localhost:8080",  # Endereço do frontend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

DATABASE_URL = "postgresql://admin:admin@localhost/intuitive_care"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/search")
def search_operadoras(
    query: str = Query(..., description="Termo para busca"),
    maxResults: int = Query(10, le=50, ge=1, description="Número máximo de resultados"),
    db: Session = Depends(get_db)
):
    # Consulta usando full-text search para obter o ranking dos resultados, considerando razao_social e nome fantasia
    sql = text("""
        SELECT *, ts_rank(
            to_tsvector('portuguese', razao_social || ' ' || nome_fantasia),
            plainto_tsquery('portuguese', :q)
        ) AS rank
        FROM relatorio_cadop
        WHERE to_tsvector('portuguese', razao_social || ' ' || nome_fantasia) @@ plainto_tsquery('portuguese', :q)
        ORDER BY rank DESC
        LIMIT :maxResults
    """)
    result = db.execute(sql, {"q": query, "maxResults": maxResults})
    registros = [dict(row._mapping) for row in result]
    return JSONResponse(content={"results": registros})
