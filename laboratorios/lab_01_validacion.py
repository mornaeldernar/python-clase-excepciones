# Archivo: lab_01_validacion.py
"""
Laboratorio 1: Validación de Datos con Excepciones
Objetivo: Practicar el manejo básico de excepciones implementando
validaciones para datos de productos.

La función debe:
1. Validar el formato y rango de los datos
2. Manejar diferentes tipos de errores
3. Proporcionar mensajes de error descriptivos
"""

def validar_producto(codigo, nombre, precio, stock):
    """
    Valida los datos de un producto
    Args:
        codigo (str): Código del producto (debe ser alfanumérico)
        nombre (str): Nombre del producto (no vacío)
        precio (float): Precio del producto (positivo)
        stock (int): Cantidad en stock (no negativo)
    Returns:
        dict: Datos del producto validados
    Raises:
        ValueError: Cuando los datos no cumplen con las validaciones
        TypeError: Cuando los tipos de datos son incorrectos
    """
    # TODO: Implementar validaciones siguiendo estos pasos:
    # 1. Validar tipos de datos
    # 2. Validar formato de código (alfanumérico)
    # 3. Validar nombre no vacío
    # 4. Validar precio positivo
    # 5. Validar stock no negativo
    
    raise NotImplementedError("¡Función no implementada!")

def main():
    # Casos de prueba
    casos_prueba = [
        {
            "codigo": "LAP001",
            "nombre": "Laptop Pro",
            "precio": 1200.50,
            "stock": 5
        },
        {
            "codigo": "123",  # Código no alfanumérico
            "nombre": "",     # Nombre vacío
            "precio": -100,   # Precio negativo
            "stock": -1       # Stock negativo
        },
        {
            "codigo": "CEL001",
            "nombre": "Smartphone X",
            "precio": "800",  # Precio como string
            "stock": "3"      # Stock como string
        }
    ]
    
    print("=== Validación de Datos de Productos ===")
    
    for i, caso in enumerate(casos_prueba, 1):
        print(f"\nPrueba {i}:")
        print(f"Datos: {caso}")
        try:
            resultado = validar_producto(
                caso["codigo"],
                caso["nombre"],
                caso["precio"],
                caso["stock"]
            )
            print("Resultado: Datos válidos")
            print(f"Producto: {resultado}")
        except (ValueError, TypeError) as e:
            print(f"Error: {str(e)}")
        except NotImplementedError as e:
            print(f"Estado: {str(e)}")

if __name__ == "__main__":
    main()