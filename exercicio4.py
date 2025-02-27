import pandas as pd

# Arquivo disponível apenas na plataforma de exercícios EBAC
df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# Escreva seu código abaixo

# Converte a coluna desconto para string
df['Desconto'] = df['Desconto'].astype(str)

# Extrai o % da string de Desconto
df['Desconto'] = df['Desconto'].astype(str).apply(lambda x: x.split('% OFF')[0])

# print(df['Desconto'])

# Extrai o texto após a palavra Novo criando uma coluna diferente
df['Condicao_Atual'] = df['Condicao'].astype(str).apply(lambda x: x.split('|')[0].strip())

# print(df[['Condicao', 'Condicao_Atual']])
# df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split(' ')[4].strip() if len(x.split(' ')) > 1 else 'Nenhum')
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split(' ')[4] if len(x.split(' ')) > 1 else 'Nenhum')

print(df['Qtd_Vendidos'])