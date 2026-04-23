import pandas as pd
import os

def generar_archivo_json(lista_ventas, nombre_archivo):
    df = pd.DataFrame(lista_ventas)
    df.to_json(nombre_archivo, orient='records', indent=4)
    print('Se crea el archivo JSON con exito')