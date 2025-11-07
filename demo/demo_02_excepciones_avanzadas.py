# Archivo: demo_02_excepciones_avanzadas.py
"""
Demo 2: Excepciones Avanzadas
Objetivo: Mostrar conceptos avanzados de manejo de excepciones incluyendo
excepciones personalizadas y contextos de manejo de recursos.
"""

class StockError(Exception):
    """Excepción personalizada para errores de stock"""
    pass

class PrecioInvalidoError(Exception):
    """Excepción personalizada para errores de precio"""
    pass

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.stock = stock
        self.validar_precio(precio)
        self._precio = precio
    
    @staticmethod
    def validar_precio(precio):
        if precio <= 0:
            raise PrecioInvalidoError("El precio debe ser mayor que 0")
        if not isinstance(precio, (int, float)):
            raise PrecioInvalidoError("El precio debe ser un número")
    
    def actualizar_stock(self, cantidad):
        if self.stock + cantidad < 0:
            raise StockError(f"Stock insuficiente. Stock actual: {self.stock}")
        self.stock += cantidad

def demo_excepciones_avanzadas():
    print("=== Demo: Excepciones Avanzadas ===")
    
    # Ejemplo 1: Excepciones personalizadas
    print("\n1. Manejo de excepciones personalizadas:")
    try:
        laptop = Producto("Laptop Pro", -1200, 5)
        laptop.actualizar_stock(-5)  # Intentar restar más del stock disponible
    except StockError as e:
        print(f"Error de stock: {str(e)}")
    except PrecioInvalidoError as e:
        print(f"Error de precio: {str(e)}")
    
    # Ejemplo 2: Context managers (with)
    print("\n2. Uso de context managers:")
    try:
        with open("registros.txt", "w") as archivo:
            archivo.write("Registro de ventas\n")
            # El archivo se cierra automáticamente al salir del bloque with
        print("Archivo creado y cerrado correctamente")
    except IOError as e:
        print(f"Error de archivo: {str(e)}")
    
    # Ejemplo 3: Propagación de excepciones
    print("\n3. Propagación de excepciones:")
    def validar_venta(producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > producto.stock:
            raise StockError("Stock insuficiente")
    
    try:
        producto = Producto("Tablet", 500, 3)
        try:
            validar_venta(producto, -1)
        except ValueError as e:
            print(f"Error de validación: {str(e)}")
            raise  # Propaga la excepción
    except Exception as e:
        print(f"Error capturado en nivel superior: {type(e).__name__}")

if __name__ == "__main__":
    demo_excepciones_avanzadas()