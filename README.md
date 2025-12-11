# Projeto BI Docker

docker build -t bi-project .
<br>
docker run -it --rm -v "${PWD}/data:/app/data" bi-project
<br>
docker compose up --build
<br>
curl http://localhost:5000/

# O que deve ser retornado no local host:
{"status": "API BI funcionando!"}

# Para os dados das vendas:

curl http://localhost:5000/vendas
<br>
[
  {"produto":"Teclado","quantidade":4,"preco":120},
  {"produto":"Mouse","quantidade":10,"preco":60},
  ...
]



