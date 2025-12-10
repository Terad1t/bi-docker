import pandas as pd

def analisar_vendas():
    df = pd.read_csv("data/vendas.csv")

    print("Dataset carregado: ")
    print(df)
    print("\n")

    # Faturamento total do produto
    df["faturamento"] = df["quantidade"] * df["preco"]

    print("faturamento por produto: ")
    print(df [["produto", "faturamento"]])
    print("\n")

    # Total geral
    total = df ["faturamento"].sum()
    print(f"Faturamento total: R$ {total:.2f}")

if __name__ == "__main__":
    analisar_vendas()