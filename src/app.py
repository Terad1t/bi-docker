from flask import Flask, request, jsonify
from db import db
from models import Venda

app = Flask(__name__)

# Credenciais do PostgreSQL (iguais ao docker-compose)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db:5432/bi_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return {"message": "API Flask + PostgreSQL funcionando!"}

@app.route("/vendas", methods=["GET"])
def get_vendas():
    vendas = Venda.query.all()
    return jsonify([v.to_dict() for v in vendas])

@app.route("/vendas", methods=["POST"])
def create_venda():
    data = request.json
    nova = Venda(
        produto=data["produto"],
        quantidade=data["quantidade"],
        preco=data["preco"]
    )
    db.session.add(nova)
    db.session.commit()
    return nova.to_dict(), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0")
