"""
Arquivo contendo funções para utilização.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datasets = {
    'assessments': '/content/assessments.csv',
    'courses.csv': '/content/courses.csv',
    'studentAssessment': '/content/studentAssessment.csv',
    'studentInfo': '/content/studentInfo.csv',
    'studentVle': '/content/studentVle.csv',
    'vle': '/content/vle.csv'
}


# Função para verificar Se contém Dados Nulos
def constainIsNull(df): 
  return df.isnull().sum()

# Função para filtrar determinada na coluna retirando o NaN
def fillNaNColumn(df, column:str):
  return df[column].fillna(0, inplace = True)

# Função para dropar determinada coluna com o NaN
def dropColumnNaN(df, column:str):
  return df.drop(column, axis=1).corr()

#### Funções abaixo são para criações e Plotagem de Gráficos

def plotImgsHeatMap(df):

  plt.figure(figsize=(16,6))
  return sns.heatmap(data=df, annot=True)

def plotImgsScatter(df, column_x:str, column_y:str):
  
  fig = px.scatter(df, x=df.column_x, y=df.column_y)
  return fig.show()

