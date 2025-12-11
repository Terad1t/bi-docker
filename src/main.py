import pandas as pd
from sqlalchemy import create_engine

def analisar_vendas():
    df = pd.read_csv("data/vendas.csv")

    print("\nDataset carregado:")
    print(df)

    # Conexão ao PostgreSQL
    engine = create_engine("postgresql://admin:admin@db:5432/bi_db")

    # Enviar dados para o banco
    df.to_sql("vendas", engine, if_exists="replace", index=False)

    print("\nDados inseridos no PostgreSQL!\n")

    # Ler de volta do banco
    consulta = pd.read_sql("SELECT * FROM vendas", engine)
    print("Dados no Banco:")
    print(consulta)


if __name__ == "__main__":
    analisar_vendas()
