# CREAR UNA FUNCION QUE CREA N EMPLEADOS
# CON:
    # ID
    # NOMBRE Y APELLIDO
    # SALARIO BASE                                       
    # DOCUMENTO
    # FECHA DE INGRESO A LA COMPAÑIA
import random
import string
from datetime import datetime, timedelta

def generar_empleados(numero_empleados):
    empleados = [
        {'id': 1, 'nombre_apellido': 'Miguel Cardona'},
        {'id': 2, 'nombre_apellido': 'Laura Martínez'},
        {'id': 3, 'nombre_apellido': 'Carlos Gómez'},
        {'id': 4, 'nombre_apellido': 'Ana Fernández'},
        {'id': 5, 'nombre_apellido': 'Pedro Sánchez'},
        {'id': 6, 'nombre_apellido': 'Sofía Ramírez'},
        {'id': 7, 'nombre_apellido': 'Andrés Torres'},
        {'id': 8, 'nombre_apellido': 'Valentina Rojas'},
        {'id': 9, 'nombre_apellido': 'Javier Cruz'},
        {'id': 10, 'nombre_apellido': 'María Delgado'},
    ]

    fechainicial = datetime(2026, 1, 5)

    if numero_empleados <= len(empleados):
        info_empleados = []

        empleados_creados = random.sample(empleados, numero_empleados)

        for empleado in empleados_creados:
            id_empleado = empleado['id']
            nombre_apellido = empleado['nombre_apellido']
            documento = ''.join(random.sample(string.digits, 10))
            fecha_ingreso = fechainicial+timedelta(days=random.randint(0, 23))
            salario_base = random.randint(10000000, 40000000)


            detalles_empleado ={
                'id_empleado':id_empleado,
                'nombre_apellido':nombre_apellido,
                'salario_base':salario_base,
                'documento':documento,
                'fecha_ingreso':fecha_ingreso
            }

            # INYECTAR ERRORES DE CALIDAD EN LOS DATOS
            probabilidadError = random.random()

            if probabilidadError < 0.15:
                detalles_empleado['id_empleado'] = str(detalles_empleado['id_empleado'])

            elif probabilidadError < 0.30:
                detalles_empleado['nombre_apellido'] = detalles_empleado['nombre_apellido'].upper()

            elif probabilidadError < 0.40:
                detalles_empleado['salario_base'] = random.choice([None, 0, '########'])

            elif probabilidadError < 0.50:
                detalles_empleado['documento']= f"{detalles_empleado['documento']}{random.randint(10,99)}"

            elif probabilidadError < 0.60:
                detalles_empleado['fecha_ingreso'] = detalles_empleado['fecha_ingreso']+timedelta(days=random.randint(1, 365))

            elif probabilidadError < 0.70:
                detalles_empleado['nombre_apellido']=  f"{detalles_empleado['fecha_ingreso']}{detalles_empleado["nombre_apellido"]}"

            # INYECTAR DUPLICADOS
            if len(info_empleados) >= 4:
                info_empleados.append(info_empleados[0].copy())
                info_empleados.append(info_empleados[1].copy())

            info_empleados.append(detalles_empleado)
        return info_empleados
    else:
        print('Ha sobrepasado el límite de empleados por mes\nEl número maximo de empleados por mes es 10')
        return
if __name__ == '__main__':
    print('Ejecuta el archivo main.py')

