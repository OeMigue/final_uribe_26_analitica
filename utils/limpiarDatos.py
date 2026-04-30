import pandas as pd

def limpiar_datos(df):
    df_copia = df.copy()
    print(f"Filas que entran: {len(df_copia)}")

    df_copia = df_copia.explode('productos')
    print(f"Después de explode: {len(df_copia)}")

    productos_df = pd.json_normalize(df_copia['productos'])

    df_copia = df_copia.reset_index(drop=True)
    productos_df = productos_df.reset_index(drop=True)

    productos_df = productos_df.drop(columns=['fecha', 'descuento', 'precio_unitario_descuento', 'subtotal'])
    df_copia = pd.concat([df_copia, productos_df], axis=1)
    df_copia = df_copia.drop(columns=['productos'])
    print(f"Después de concat: {len(df_copia)}")

    df_copia.columns = df_copia.columns.str.strip()
    columnas_texto = ['producto', 'talla', 'vendedor']
    for columna in columnas_texto:
        df_copia[columna] = df_copia[columna].astype(str).str.strip()

    df_copia['producto'] = df_copia['producto'].str.title()
    df_copia['vendedor'] = df_copia['vendedor'].str.title()
    df_copia['talla'] = df_copia['talla'].str.upper()

    df_copia.replace(['', 'None', 'nan'], pd.NA, inplace=True)

    df_copia['precio'] = pd.to_numeric(df_copia['precio'], errors='coerce')
    df_copia['cantidad'] = pd.to_numeric(df_copia['cantidad'], errors='coerce')
    df_copia['total'] = pd.to_numeric(df_copia['total'], errors='coerce')
    df_copia['fecha'] = pd.to_datetime(df_copia['fecha'], errors='coerce', dayfirst=True)
    print(f"Después de convertir tipos: {len(df_copia)}")

    df_copia = df_copia.drop_duplicates()
    print(f"Después de drop_duplicates: {len(df_copia)}")

    df_copia = df_copia.dropna(subset=['producto', 'precio', 'cantidad', 'fecha'])
    print(f"Después de dropna: {len(df_copia)}")

    df_copia = df_copia[df_copia['cantidad'] > 0]
    print(f"Después de filtrar cantidad: {len(df_copia)}")

    df_copia = df_copia[df_copia['precio'] > 15000]
    print(f"Después de filtrar precio: {len(df_copia)}")

    tallas_validas = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL']
    df_copia = df_copia[df_copia['talla'].isin(tallas_validas)]
    print(f"Después de filtrar tallas: {len(df_copia)}")

    df_copia['total'] = df_copia['cantidad'] * df_copia['precio']

    return df_copia