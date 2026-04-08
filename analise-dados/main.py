import pandas as pd

df = pd.read_csv('data/vendas.csv')

df['total'] = df['preco'] * df['quantidade']

faturamento = df['total'].sum()
mais_vendido = df.groupby('produto')['quantidade'].sum().idxmax()

print("Faturamento total:", faturamento)
print("Produto mais vendido:", mais_vendido)