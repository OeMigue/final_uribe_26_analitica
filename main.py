import sys
from tabulate import tabulate
import pandas as pd
from data.simuladorVentas import generar_ventas
from data.simuladorEmpleados import generar_empleados
sys.stdout.reconfigure(encoding='utf-8')

def main():
    lista_ventas = generar_ventas(5)
    df_ventas = pd.DataFrame(lista_ventas)
    print(df_ventas)

    lista_empleados = generar_empleados(10)
    df_empleados = pd.DataFrame(lista_empleados)
    print(df_empleados)

if __name__ == '__main__':
    main()