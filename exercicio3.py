import pandas as pd

# Arquivo disponível apenas na plataforma de exercícios EBAC
df = pd.read_csv('/data/ecommerce_ex3.csv')

# Escreva seu código abaixo

# print(df.dtypes)

# # Calcular o intervalo interquartil (IQR)
q1 = df['N_Avaliacoes'].quantile(0.25)
q3 = df['N_Avaliacoes'].quantile(0.75)
iqr = q3 - q1

# print(iqr)

# # Definir o limite superior para identificar outliers
limite_alto = q3 + 1.5 * iqr

# print(limite_alto)

# # Filtrar os produtos que possuem um número de avaliações maior que o limite superior
df_avaliados = df[df['N_Avaliacoes'] >= limite_alto]

print('Quantidade de linhas:', df.shape[0])
print('Quantidade de linhas:', df_avaliados.shape[0])