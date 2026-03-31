# FUNCION GENERADORA DE N VENTAS QUE PERMITA CREAR MOCKS O DATOS SEMILLA PARA LA RUTINA DE ANAISIS
import random
from datetime import datetime, timedelta

def generar_ventas(numero_ventas, limite_productos=5):
    
    # SIMULAR UNA LISTA DE PRODUCTOS
    # PARA OPTIMIZAR:
        # LEER UN EXCEL Y CARGAR UNA LISTA CON SU INFO
        # CONSUMIR API

    productos  = [
        {'nombre':'Chaqueta de Mujer Shacket Silueta Amplia Denim Liviano con Parches Varsity en Algodón', 'precio':150000, 'descuento':True},
        {'nombre':'Vestido Casual de Algodón con Estampado Floral y Cinturón Ajustable', 'precio':82000, 'descuento':False},
        {'nombre':'Zapatos Deportivos Running Unisex con Suela Antideslizante y Malla Transpirable', 'precio':98000, 'descuento':True},
        {'nombre':'Camisa Formal Slim Fit Manga Larga en Lino Texturizado para Hombre', 'precio':76000, 'descuento':False},
        {'nombre':'Pantalón Cargo Multibolsillos con Cintura Elástica y Cordón Ajustable', 'precio':68000, 'descuento':True},
        {'nombre':'Blusa de Satén Brillante con Cuello Mao y Mangas Globo', 'precio':54000, 'descuento':False},
        {'nombre':'Suéter Oversize de Punto Grueso con Cuello Alto y Diseño Trenzado', 'precio':90000, 'descuento':True},
        {'nombre':'Bolso Tote Ecológico de Yute con Forro Interior y Bolsillo Interno', 'precio':42000, 'descuento':False},
        {'nombre':'Reloj Analógico Minimalista con Correa de Acero Inoxidable y Esfera Negra', 'precio':125000, 'descuento':True},
        {'nombre':'Gafas de Sol UV400 Estilo Aviador con Montura Metálica y Lentes Polarizadas', 'precio':65000, 'descuento':False}
    ]

    # SIMULAR LISTA DE TALLAS 
    tallas  = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL',]

    # SIMULAR VENDEDOR ASOCIADO
    vendedores = ['Miguel Cardona', 'Nicolás Parra', 'Sebastian Gómez', 'Ana Gómez', 'Carlos Mejía', 'Mariana Díaz', 'Andrés Vargas', 'Esteban Agudelo', 'Diego Castillo', 'Valeria López']

    # SIMULAR FECHA
    fechaInicio =datetime(2026,1,2)

    # GENERAR LAS N VENTAS QUE ME PIDEN
    ventas=[]
    for _ in range(numero_ventas):
        cantidad_productos = random.randint(1, limite_productos)

        productos_seleccionados = random.sample(productos, cantidad_productos) #¿Cómo hago para agregar mas de un producto a la simulacion?

        for producto in productos_seleccionados:
            cantidad = random.randint(1,5)
            precio = producto['precio']
            fecha =fechaInicio+timedelta(days=random.randint(0,60))
        ventas.append(
            {
                'producto': producto['nombre'],
                'precio': precio,
                'talla':random.choice(tallas),
                'cantidad':cantidad,
                'vendedor':random.choice(vendedores),
                'fecha':fecha,
                'total':cantidad*precio
            } 
        )
    return ventas