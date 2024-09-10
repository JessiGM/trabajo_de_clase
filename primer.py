"""
num1 = input() #este input es para recibir el valor que el usuario pone
num2 = 2
num3 = int(3)
print("Este es el número ingresado por el usuario", num1) #para imprimir lo que vale
#esta variable, en este caso lo que pone el usuario
# se concatena con ,
print (f'Este es el número ingresado por el usuario {num1}') #de esta forma también
#se puede imprimir
print(type(num1)) #para conocer el tipo de dato de la variable
print(type(num2),type(num1), type(num3)) #así para reducir código
"""
"""
num1 = 6
num2 = 34
if (num1 >= num2) or (num1 <= num2):
    print(f'{num1} es mayor') #falta poner mensaje por el cambio de la condición
elif num1 == num2:
    print("Son iguales")
else:
    print("No se cumple ninguna condición")
"""

"""
num1 = int (input("Por favor ingrese el primer número"))
num2 = int (input("Por favor ingrese el segundo número"))
operacion = int(input("¿Que operación desea realizar?: 1=suma, 2=resta, 3=multiplicación"))

if operacion == 1:
    print(num1+num2)
elif operacion == 2:
    print(num1-num2)
elif operacion == 3:    
    print(num1*num2)
else:    
    print("Ingrese un número válido")
"""

pal1 = input("Por favor ingrese la primer palabra: ")
pal2 = input("Por favor ingrese la segunda palabra: ")
pal3 = input("Por favor ingrese la tercer palabra: ")
pal4 = input("Por favor ingrese la cuarta palabra: ")

if (pal1 > pal2) and (pal1 > pal3) and (pal1 > pal4):
    print("La palabra # 1 es la mayor")
elif (pal2 > pal1) and (pal2 > pal3) and (pal2 > pal4):
    print("La palabra # 1 es la mayor")


    #terminar este ejercicio
elif operacion == 3:    
    print(num1*num2)
else:    
    print("Ingrese un número válido")
