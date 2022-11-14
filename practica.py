#Muestra un grafico de uso de m3 y de número de clientes

import pandas as pd
import matplotlib.pyplot as plt

def mostrar_grafico():

    datos = pd.read_csv("C:\\Users\\Tecnicos\\PycharmProjects\\Teoria14112022\\servicioagua.csv")
    df = datos[["m3_registrats", "núm_clients"]]

    df = datos.rename(columns={
            "m3_registrats": "m3",
            "núm_clients": "NÚMERO_CLIENTES"
        })

    #Grafico circular
    df.NÚMERO_CLIENTES.value_counts().plot.pie()
    plt.show()

    #Histograma
    df.m3.plot.hist()
    plt.show()
mostrar_grafico()