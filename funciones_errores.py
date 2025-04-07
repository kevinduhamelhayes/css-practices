# Funciones y manejo de errores en Python

# Función básica
def saludar(nombre):
    return f"¡Hola, {nombre}!"

print(saludar("Python"))

# Función con argumentos por defecto
def calcular_area(base, altura=1):
    return base * altura

print(f"Área: {calcular_area(5)}")  # Usa altura por defecto
print(f"Área: {calcular_area(5, 3)}")  # Usa altura especificada

# Función con argumentos variables
def sumar(*numeros):
    return sum(numeros)

print(f"Suma: {sumar(1, 2, 3, 4, 5)}")

# Manejo de errores con try-except
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"
    except TypeError:
        return "Error: Los argumentos deben ser números"
    else:
        return resultado
    finally:
        print("Operación completada")

print(dividir(10, 2))
print(dividir(10, 0))
print(dividir("10", 2))

# Función con documentación
def factorial(n):
    """
    Calcula el factorial de un número.
    
    Args:
        n (int): Número entero positivo
        
    Returns:
        int: El factorial de n
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial de 5: {factorial(5)}") 