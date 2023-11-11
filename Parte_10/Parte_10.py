import sys
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from sklearn.manifold import TSNE
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def getRequestCSV(url: str):
    try:
        response = requests.get(url)
        if(response.status_code == requests.codes.ok):
            with open('datos.csv', 'wb') as archivo_local:
                archivo_local.write(response.content)
            return True
        else:
            return False
    except:
        return False


def processData(dataframe: pd.DataFrame):
    dataSinFaltantes = dataframe.dropna()
    dataSinFaltantes.drop_duplicates(inplace=True)
    dataSinAtipicos = dataSinFaltantes.copy()
    for columna in dataSinAtipicos.columns:
        if dataSinAtipicos[columna].dtype in ['int64', 'float64']:
            Q1 = dataSinAtipicos[columna].quantile(0.25)
            Q3 = dataSinAtipicos[columna].quantile(0.75)
            IQR = Q3 - Q1
            limite_inferior = Q1 - 1.5 * IQR
            limite_superior = Q3 + 1.5 * IQR
            dataSinAtipicos = dataSinAtipicos[(dataSinAtipicos[columna] >= limite_inferior) & (dataSinAtipicos[columna] <= limite_superior)]
    dataSinAtipicos['ageCategory'] = pd.cut(dataSinAtipicos['age'], bins=[0, 12, 19, 39, 59, float('inf')], labels=['Niño', 'Adolescente', 'Joven adulto', 'Adulto', 'Adulto mayor'])
    dataSinAtipicos.to_csv('datosProcesados.csv', index=False)



data = pd.read_csv('datosProcesados.csv')
X = data.drop(columns=['DEATH_EVENT', 'age', 'ageCategory'])
y = data['age']

regression = LinearRegression()
regression.fit(X, y)

y_predict = regression.predict(X)
mse = mean_squared_error(y, y_predict)
print(mse)