def es_par(numero):
    #Devuelve True si el número es par, False si es impar.
    return numero % 2 == 0

def numeros_facultad():
    num_pares = 0
    num_impares = 0
    listado = []

    # Pedir 400 números al usuario
    for i in range(400):
        while True:
            try:
                numero = int(input(f"Introduce el número {i + 1}: "))
                break
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entero.")

        if es_par(numero):
            tipo = "Par"
            num_pares += 1
        else:
            tipo = "Impar"
            num_impares += 1

        listado.append((numero, tipo))

    # Mostrar el listado de números con su tipo
    print("\nListado de números:")
    print(f"{'Número':<10} {'Tipo':<10}")
    print("="*20)
    for numero, tipo in listado:
        print(f"{numero:<10} {tipo:<10}")

    # Mostrar el conteo de números pares e impares
    print("\nResumen:")
    print(f"Números pares: {num_pares}")
    print(f"Números impares: {num_impares}")

# Llamar a la función directamente
numeros_facultad()
