"""
Arquivo contendo funções para utilização.
"""


# Função para verificar Se contém Dados Nulos
def constainIsNull(df): 
  return df.isnull().sum()

# Função para filtrar determinada na coluna retirando o NaN
def filNaNColumn(df, column:str):
  return df[column].fillna(0, inplace = True)

# Função para dropar determinada coluna com o NaN
def dropColumnNaN(df, column:str):
  return df.drop(column, axis=1).corr()

