#Actividad 14
#https://naps.com.mx/blog/ejemplos-en-matplotlib-de-5-tipos-graficos/

#Fuente de datos (3)-->
    # 1. Archivo (txt, csv...)
    # 2. Base de datos (sql (mysql) y nosql (mongodb))
    # 3. Web Services, API Rest : petición get : response xml / json

import pandas as pd
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def cargar_archivo():
    datos = pd.read_csv("C:\\Users\\Tecnicos\\Downloads\\casasboston.csv")
    # datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
    df = datos[["RM", "CRIM", "MEDV", "TOWN", "CHAS"]] #Selecciona algunas columnas

    df = datos.rename(columns={
        "TOWN": "CIUDAD",
        "CRIM": "INDICE_CRIMEN",
        "INDUS": "PCT_ZONA_INDUSTRIAL",
        "CHAS": "RIO_CHARLES",
        "RM": "N_HABITACIONES_MEDIO",
        "MEDV": "VALOR_MEDIANO",
        "LSTAT": "PCT_CLASE_BAJA"
    })

    #print(df.sample(5))

    #Histograma
    df.N_HABITACIONES_MEDIO.plot.hist()
    plt.show()

    #Grafico de dispersión
    df.plot.scatter(x="INDICE_CRIMEN", y="VALOR_MEDIANO", alpha=0.1)
    plt.show()

    #Grafico de barras
    valor_por_ciudad = df.groupby("CIUDAD")["VALOR_MEDIANO"].mean()
    valor_por_ciudad.head(10).plot.barh()
    plt.show()

    #Grafico de cajas
    df["VALOR_CUANTILES"] = pd.qcut(df.VALOR_MEDIANO, 5)
    df.boxplot(column="INDICE_CRIMEN", by="VALOR_CUANTILES",
               figsize=(8, 6))
    plt.show()

    #Grafico circular
    df.RIO_CHARLES.value_counts().plot.pie()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    cargar_archivo()
