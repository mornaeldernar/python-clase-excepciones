# Archivo: demo_01_excepciones.py
"""
Demo 1: Manejo Básico de Excepciones
Objetivo: Mostrar los conceptos fundamentales del manejo de excepciones en Python
usando ejemplos prácticos de validación de datos.
"""

def demo_excepciones():
    print("=== Demo: Manejo Básico de Excepciones ===")
    
    # Ejemplo 1: Try-except básico
    print("\n1. Manejo básico de errores:")
    try:
        precio = float(input("Ingrese un precio: "))
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        print(f"Precio válido: ${precio}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    
    # Ejemplo 2: Múltiples excepciones
    print("\n2. Manejando múltiples tipos de error:")
    productos = {"laptop": 1200, "smartphone": 800}
    try:
        producto = input("Ingrese nombre del producto: ")
        cantidad = int(input("Ingrese cantidad: "))
        precio_total = productos[producto] * cantidad
        print(f"Total a pagar: ${precio_total}")
    except KeyError:
        print("Error: Producto no encontrado")
    except ValueError:
        print("Error: Cantidad debe ser un número")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
    
    # Ejemplo 3: Finally
    print("\n3. Uso de finally:")
    archivo = None
    try:
        archivo = open("ventas.txt", "r")
        contenido = archivo.read()
        print(contenido)
    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    finally:
        if archivo:
            archivo.close()
            print("Archivo cerrado correctamente")

if __name__ == "__main__":
    demo_excepciones()