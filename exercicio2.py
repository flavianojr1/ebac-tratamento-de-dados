import pandas as pd

# Arquivo disponível apenas na plataforma de exercícios EBAC
df = pd.read_csv('/data/ecommerce_ex2.csv')

# Escreva seu código abaixo


print('Quantidade de linhas:', df.shape[0])
# Converter a coluna 'Marca' para letras minúsculas
df['Marca'] = df['Marca'].str.lower()
# print('Marcas em minusculo:', df['Marca'])

# Converter a coluna 'Material' para letras minúsculas
df['Material'] = df['Material'].str.lower()
# print('Materiais em minusculo:', df['Material'])

# Converter a coluna 'Temporada' para letras minúsculas
df['Temporada'] = df['Temporada'].str.lower()
# print('Temporada em minusculo:', df['Temporada'])

# Remover linhas duplicadas
df = df.drop_duplicates()

# Remover linhas com menos de 8 valores não nulos
# O parâmetro 'thresh' define o número mínimo de valores não nulos necessários para manter a linha
df = df.dropna(thresh=8)
print('Quantidade de linhas:', df.shape[0])
