import pandas as pd

arquivo = input("Digite o caminho do arquivo CSV: ")
df = pd.read_csv(arquivo)

df['total'] = df['preco'] * df['quantidade']

faturamento = df['total'].sum()
mais_vendido = df.groupby('produto')['quantidade'].sum().idxmax()
ranking = df.groupby('produto')['quantidade'].sum().sort_values(ascending=False)
ticket_medio = df['total'].mean()

print("Faturamento total:", faturamento)
print("Produto mais vendido:", mais_vendido)
print("\nRanking de vendas:")
print(ranking)
print("\nTicket médio:", round(ticket_medio, 2))

import matplotlib.pyplot as plt

vendas = df.groupby('produto')['quantidade'].sum()
plt.figure(figsize=(8,5))
vendas.plot(kind='bar')

plt.title('Produtos mais vendidos')
plt.xlabel('Produto')
plt.ylabel('Quantidade')

plt.show()

ranking.plot(kind='bar')
plt.title('Ranking de Produtos')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.show()

# Salvar relatório em CSV
df.to_csv('data/relatorio.csv', index=False)

print("\nRelatório salvo em data/relatorio.csv")