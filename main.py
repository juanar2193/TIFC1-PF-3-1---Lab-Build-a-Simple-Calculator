# Write a program that takes two input numbers, then adds them together and prints the result.
a = int(input())
b = int(input())
print(a + b)

# ---------------- Extra time ----------------
print("\nOperaciones extra")
print("Elige una operacion: +  -  *  /  %")
operacion = input()
 
x = float(input("Primer numero: "))
y = float(input("Segundo numero: "))
 
if operacion == "+":
    print(x + y)
elif operacion == "-":
    print(x - y)
elif operacion == "*":
    print(x * y)
elif operacion == "/":
    if y == 0:
        print("No se puede dividir entre cero")
    else:
        print(x / y)
elif operacion == "%":
    print(x % y)
else:
    print("Operacion no valida")
 
# Sumar 3 numeros
print("\nSuma de tres numeros")
n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))
print(n1 + n2 + n3)
 
# Mezclar operaciones, por ejemplo: 2 + 4 - 3  o  4 * 5 + 1 / 3
print("\nEscribe una operacion con varios numeros")
texto = input()
print(eval(texto))