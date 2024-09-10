
"""
#ejercicio 1 - tabla de multiplicar de un número
num1 = int(input("Esto es una multiplicación, ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

res_mult = num1 * num2
print("El resultado de la multiplicación de " , num1 , " por " , num2 , " es: " , mult)
"""

"""
#ejercicio 2 - tabla de potencias de un número
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese el segundo número entero para la potencia: "))

res_poten = pow(num1, num2)
print("El resultado de la potencia es: " , res_poten)
"""

"""
#ejercicio 3 - números crecientes
num1 = int(input("Ingrese el número inicial: "))
num2 = int(input("Ingrese el número final: "))

for i in range(num1, num2 + 1):
    print(i)
"""

"""
#ejercicio 4 - números decrecientes
num1 = int(input("Ingrese el número inicial: "))
num2 = int(input("Ingrese el número final: "))

for i in range(num1, num2 - 1, -1):
    print(i)
"""

"""
#ejercicio 5 - imprimir números pares hasta número n
num = int(input("Ingrese un número: "))
for i in range(0, num + 1, 2):
    print(i)
"""

"""
#ejercicio 6 - imprimir números primos hasta número n
num = int(input("Ingrese un número: "))

def num_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def imprimir_primos(hasta):
    for i in range(2, hasta + 1):
        if num_primo(i):
            print(i)

imprimir_primos(num)
"""

"""
#ejercicio 7 - mostrar palabra n cantidad de veces
pal = str(input("Ingrese una palabra por favor: "))
cant = int(input("Ingrese la cantidad de veces que desea ver la palabra: "))

resul = ' '.join([pal]*cant)
print(resul)
"""

"""
#ejercicio 8 - mostrar los años en que ha cumplido
#este está en inglés las variables para no escribir ano jajajajaj
from datetime import datetime

actual_age = int(input("Ingrese su edad: "))
actual_year = datetime.now().year

for age in range(actual_age + 1):
    birthday = actual_year - (actual_age - age)
    print("A los " , age , " años, fue el año " , birthday)
"""

"""
#ejercicio 9 - n numero entero positivo y mostrar los números impares hasta n número ","
num = int(input("Ingrese un número entero positivo: "))

if num >= 0:
    impares = []
    for i in range(1, num + 1):
        if i % 2 !=0:
            impares.append(str(i))
    result = ', '.join(impares)
    print(result)
else:
    print("Por favor ingrese un número válido")
"""

"""
#ejercicio 10 - n número entero positivo con cuenta atrás hasta cero " ,"
num = int(input("Ingrese un número entero positivo: "))

if num >= 0:
    nums = []
    for i in range(num, -1, - 1):
        nums.append(str(i))
    result = ', '.join(nums)
    print(result)
else:
    print("Por favor ingrese un número válido")
"""

"""
#ejercicio 11 - cantidad a invertir, interés anual, cantidad de años, capital anual
capital_inicial = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (en porcentaje): ")) / 100
cant_years = int(input("Ingrese el número de años: "))

print("\nAño\tCapital")

for year in range(1, cant_years + 1):
    capital = capital_inicial * (1 + interes_anual) ** year
    print(f"{year}\t{capital:.2f}")
"""