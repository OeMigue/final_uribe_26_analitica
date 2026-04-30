import sys
import pandas as pd
from data.simuladorVentas import generar_ventas
from data.simuladorEmpleados import generar_empleados
from utils.generarCSV import generar_archivo_csv
from utils.generarJSON import generar_archivo_json
from utils.limpiarDatos import limpiar_datos
sys.stdout.reconfigure(encoding='utf-8')

pd.set_option('display.max_columns', None)   # Muestra todas las columnas
# pd.set_option('display.max_rows', None)      # Muestra todas las filas
pd.set_option('display.width', None)         # No corta el ancho
# pd.set_option('display.max_colwidth', None)  # No corta el texto de las celdas

def main():
    lista_ventas = generar_ventas(10)
    df_ventas = pd.DataFrame(lista_ventas)
    print(df_ventas)

    datos_limpios = limpiar_datos(df_ventas)
    print(datos_limpios)

    # lista_empleados = generar_empleados(10)
    # df_empleados = pd.DataFrame(lista_empleados)
    # print(df_empleados)

    # generando un dataset en formato csv
    # generar_archivo_csv(lista_ventas, 'data/ventas_sucias.csv')

    # generabndo un dataset en formato json
    generar_archivo_json(lista_ventas, 'data/json_ventas.json')
    generar_archivo_json(datos_limpios, 'data/json_ventas_limpias.json')


    # RUTINA DE LIMPIEZA DE DATOS / Evaluar calidad de los datos
    # ¿Qué se limpia?
    #   A) NOMBRES DE LAS COLUMNAS
    
    #   B) TEXTOS - ESPACIOS - MAYUSCULAS/MINUSCULAS - FORMATOS INCONSISTENTES

    #   C) VALORES NULOS

    #   D) VALORES SUPLICADOS

    #   E) VERIFICAR EL TIPO DE DATOS

    #   F) SE VERIFICAN LAS REGLAS DE NEGOCIO



if __name__ == '__main__':
    main()