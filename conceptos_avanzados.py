# Conceptos avanzados de Python

# Decoradores
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función")
        resultado = func(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado
    return wrapper

@mi_decorador
def saludar(nombre):
    return f"¡Hola, {nombre}!"

print(saludar("Python"))

# Generadores
def generador_pares(limite):
    for i in range(limite):
        if i % 2 == 0:
            yield i

print("\nNúmeros pares:")
for par in generador_pares(10):
    print(par)

# Context Managers
class MiContextManager:
    def __enter__(self):
        print("Entrando al contexto")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del contexto")
    
    def hacer_algo(self):
        print("Haciendo algo dentro del contexto")

print("\nUsando context manager:")
with MiContextManager() as cm:
    cm.hacer_algo()

# Expresiones lambda
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"\nCuadrados usando lambda: {cuadrados}")

# Filtrado con lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares usando lambda: {pares}")

# Clases abstractas
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado

mi_cuadrado = Cuadrado(5)
print(f"\nÁrea del cuadrado: {mi_cuadrado.calcular_area()}")
print(f"Perímetro del cuadrado: {mi_cuadrado.calcular_perimetro()}") 