from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Conexão com PostgreSQL
engine = create_engine("postgresql://admin:admin@db:5432/bi_db")

@app.get("/")
def home():
    return {"status": "API BI funcionando"}

@app.get("/vendas")
def listar_vendas():
    # Consulta os dados do banco
    df = pd.read_sql("SELECT * FROM vendas", engine)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
