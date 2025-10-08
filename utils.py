"""
Arquivo contendo funções para utilização.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Função para verificar Se contém Dados Nulos
def constainIsNull(df): 
  return df.isnull().sum()

# Função para filtrar determinada na coluna retirando o NaN
def filNaNColumn(df, column:str):
  return df[column].fillna(0, inplace = True)

# Função para dropar determinada coluna com o NaN
def dropColumnNaN(df, column:str):
  return df.drop(column, axis=1).corr()


