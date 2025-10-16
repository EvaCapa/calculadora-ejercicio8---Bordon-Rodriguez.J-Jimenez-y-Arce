import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

def potenciacion(a, b):
    return a ** b

def radicacion(a, b):
    if a >= 0:
        return a ** (1 / b)
    else:
        return "No se puede calcular la raíz de un número negativo"

def porcentaje(a, b):
    return (a * b) / 100

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "No se puede calcular módulo con divisor cero"

def factorial(a):
    if a >= 0 and int(a) == a:
        return math.factorial(int(a))
    else:
        return "No se puede calcular factorial de número negativo o no entero"

num1 = 5
num2 = 2

print("Calculadora extendida")
print("Suma:", suma(num1, num2))
print("Resta:", resta(num1, num2))
print("Multiplicación:", multiplicacion(num1, num2))
print("División:", division(num1, num2))
print("Potenciación:", potenciacion(num1, num2))
print("Radicación:", radicacion(num1, num2))
print("Porcentaje:", porcentaje(num1, num2))
print("Módulo:", modulo(num1, num2))
print(f"Factorial de {num1}:", factorial(num1))
