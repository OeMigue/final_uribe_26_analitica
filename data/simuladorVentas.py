# FUNCION GENERADORA DE N VENTAS QUE PERMITA CREAR MOCKS O DATOS SEMILLA PARA LA RUTINA DE ANAISIS
import random
import string
import sys
from datetime import datetime, timedelta

sys.stdout.reconfigure(encoding='utf-8')

def generar_ventas(numero_ventas, limite_productos=6):
    
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
    DESCUENTO = 0.40
    for _ in range(numero_ventas):
        detalle_productos = []
        total_venta = 0
        fecha =fechaInicio+timedelta(days=random.randint(0,60))

        cantidad_productos = random.randint(1, limite_productos)        

        productos_seleccionados = random.sample(productos, min(cantidad_productos, len(productos)))

        for producto in productos_seleccionados:
            cantidad = random.randint(1, 3)
            precio = producto['precio']
            if producto['descuento'] == True:
                precio_final = precio * (1 - DESCUENTO)
            else:
                precio_final = precio
            subtotal = precio_final * cantidad
            
            detalle_productos.append(
                {
                    'producto': producto['nombre'],
                    'precio': precio,
                    'talla':random.choice(tallas),
                    'cantidad':cantidad,
                    'descuento':producto['descuento'],
                    'precio_unitario_descuento': precio_final,
                    'subtotal':subtotal,
                    'fecha': fecha
                } 
            )
            total_venta += precio_final
            venta={
                'productos': detalle_productos,
                'vendedor': random.choice(vendedores),
                'fecha':fecha,
                'total': total_venta
            }
            # INYECTAR ERRORES DE CALIDAD EN LOS DATOS 
            probabilidadError = random.random()

            if probabilidadError < 0.15:
                venta['productos'][0]['producto'] = f" {venta['productos'][0]['producto']} "
            elif probabilidadError < 0.30:
                venta['vendedor'] = venta['vendedor'].upper()
            elif probabilidadError < 0.40:
                venta['productos'][0]['talla'] = 'medio'
            elif probabilidadError < 0.50:
                venta['productos'][0]['cantidad'] = random.choice([0, -1, None])
            elif probabilidadError < 0.60:
                venta['productos'][0]['precio'] = None
            elif probabilidadError < 0.70:
                venta['fecha'] = fecha.strftime("%d/%m/%Y")
            elif probabilidadError < 0.80:
                venta['total'] = random.randint(1000, 5000)
            elif probabilidadError < 0.90:
                venta['productos'][0]['producto'] = venta['productos'][0]['producto'].lower()
            
        ventas.append(venta)
    # Inyectar datos duplicados
    if len(ventas)>= 6:
        ventas.append(ventas[0].copy())
        ventas.append(ventas[1].copy())
    return ventas
