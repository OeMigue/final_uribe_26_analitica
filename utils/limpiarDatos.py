import pandas as pd

def limpia_datos(df):
    df_copia = df.copy()

    df_copia.columns=df_copia.columns.str.strip()
    columnas_texto = ['productos', 'talla', 'vendedor']
    for columna in columnas_texto:
        df_copia[columna] = df_copia[columna].astype(str).str.strip()

    df_copia['producto'] = df_copia['producto'].str.title()
    df_copia['vendedor'] = df_copia['vendedor'].str.title()
    df_copia['talla'] = df_copia['talla'].str.upper()

    df_copia.replace(['', 'None', 'nan'], pd.NA, inplace=True) 

    df_copia['precio'] = pd.to_numeric(df_copia['precio'], errors='coerce')
    df_copia['cantidad'] = pd.to_numeric(df_copia['cantidad'], errors='coerce')
    df_copia['total'] = pd.to_numeric(df_copia['total'], errors='coerce')

    df_copia['fecha'] = pd.to_datetime(df_copia['fecha'], errors='coerce')

    df_copia = df_copia.drop_duplicates()

    df_copia = df_copia.dropna(subset=['producto', 'precio', 'cantidad', 'fecha'])

    # RUTINA PARA LIMPIAR SEGUN LA REGLA DE NEGOCIO

    df_copia= df_copia[df_copia['cantidad']>0]
    df_copia= df_copia[df_copia['precio']>15000]

    tallas_validas = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL']

    df_copia=df_copia[df_copia['talla'].isin(tallas_validas)]
    df_copia['total'] = df_copia['cantidad']*df_copia['precio']