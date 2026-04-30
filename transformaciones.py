import pandas as pd
from data.simuladorVentas import generar_ventas
from utils.limpiarDatos import limpiar_datos

pd.set_option('display.max_columns', None)   # Muestra todas las columnas
pd.set_option('display.width', None)         # No corta el ancho


# Transformando datos en funcion de decisiones utiles para el negocio

# PANDAS => QUERIES (Condiciones lógicas que permiten extraer información de un set de datos)
datos = generar_ventas(100) #--> Datos sucios ---> Pasar por funcion de limpieza
df_ventas = pd.DataFrame(datos)

datos_limpios = limpiar_datos(df_ventas)

# print(f"DATOS SUCIOS\n{df_ventas}\n")
# print(f"DATOS LIMPIOS\n{datos_limpios}")

# 1. QUERY simple 
# Averiguar cuales son las ventas superiores a 500.000 pesos
ventas_mayores_500 = datos_limpios.query('total > 100000')
# print(ventas_mayores_500)

# 2. QUERY CON 2 CONDICIONES
# FILTAR FILAS DONDE EL TOTAL SEA MAYOR A 300MIL Y LA TALLA SEA M
ventas_300_tallaM = datos_limpios.query("total > 70000 and talla == 'M'" )
# print(ventas_300_tallaM)

# QUERYES CON VALORES ESPECIFICOS DE UNA COLUMNA 
# Me gustaria ver de Miguel, Nico o Sebas
ventas_vendedor1 = datos_limpios.query("vendedor == 'Miguel Cardona'").head(5)
ventas_vendedor2 = datos_limpios.query("vendedor == 'Nicolas Parra'").head(5)
ventas_vendedor3 = datos_limpios.query("vendedor == 'Sebastian Gomez'").head(5)
print(ventas_vendedor1, ventas_vendedor2, ventas_vendedor3)

# 4. OTRAS QUERYES DPENDOENDO DEL NEGOCIO QUE ESTOY ANALIZANDO 
# Filtrar las filas cuyo valor en la columna mes sea igual a 2, Recuperar las ventas del mes de febrero
# Analizando (Trnsformando) fechas con pandas
datos_limpios["fecha"] = pd.to_datetime(datos_limpios['fecha'], errors="coerce", dayfirst=False)

# ventas_febrero = datos_limpios.query('fecha ')