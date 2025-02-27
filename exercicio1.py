import pandas as pd

# Arquivo disponível apenas na plataforma de exercícios EBAC
df = pd.read_csv('/data/ecommerce.csv')

# Verifique a quantidade de linhas e colunas
linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

# Verifique os tipos de dados
tipos = df.dtypes
print('\nVerificar Tipagem:\n', tipos)

# Verifique a quantidade de valores nulos
nulos = df.isnull().sum()
print('\nVerificar valores nulos:\n', nulos)

#  Substitua os valores nulos das colunas ‘Temporada’ e ‘Marca’ por ‘Não Definido’

# print('\n Teste:\n{}'.format(df[['Temporada', 'Marca']]))

df.fillna({'Temporada': 'Não Definido', 'Marca': 'Não Definido'}, inplace=True)