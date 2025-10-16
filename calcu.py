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

print("Calculadora básica")
print("Suma:", suma(4, 2))
print("Resta:", resta(4, 2))
print("Multiplicación:", multiplicacion(4, 2))
print("División:", division(4, 2))
