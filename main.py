from data.simuladorVentas import generar_ventas

def main():
    try:
        print(generar_ventas(5))
    except Exception as e:
        print(f'❌ERROR: {e}')

if __name__ == '__name__':
    main()