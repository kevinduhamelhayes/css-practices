# Programación Orientada a Objetos en Python

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    
    def hacer_sonido(self):
        return "¡Guau!"
    
    def __str__(self):
        return f"Perro: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}"

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def hacer_sonido(self):
        return "¡Miau!"
    
    def __str__(self):
        return f"Gato: {self.nombre}, Color: {self.color}, Edad: {self.edad}"

# Crear instancias
mi_perro = Perro("Rex", 3, "Labrador")
mi_gato = Gato("Michi", 2, "Negro")

# Usar los métodos
print(mi_perro)
print(f"Sonido del perro: {mi_perro.hacer_sonido()}")

print(mi_gato)
print(f"Sonido del gato: {mi_gato.hacer_sonido()}")

# Polimorfismo
animales = [mi_perro, mi_gato]
for animal in animales:
    print(f"{animal.nombre} hace: {animal.hacer_sonido()}") 