# Estructuras de control en Python

# Condicional if-elif-else
edad = 18
if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Acabas de cumplir la mayoría de edad")
else:
    print("Eres mayor de edad")

# Bucle for
print("\nBucle for:")
for i in range(5):
    print(f"Valor de i: {i}")

# Bucle while
print("\nBucle while:")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Break y continue
print("\nUso de break y continue:")
for i in range(10):
    if i == 3:
        continue  # Salta la iteración actual
    if i == 7:
        break    # Termina el bucle
    print(f"Valor: {i}")

# List comprehension
print("\nList comprehension:")
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(f"Cuadrados: {cuadrados}") 