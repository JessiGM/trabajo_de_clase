def clasificar_funcionamiento(puntaje):
    # Clasificar el funcionamiento de la cabina basado en el puntaje.
    if puntaje == 2:
        return "Funcionamiento Defectuoso"
    elif puntaje == 3:
        return "Funcionamiento Moderado"
    elif puntaje == 4:
        return "Funcionamiento Óptimo"
    else:
        return "Puntaje fuera del rango esperado"

# Función para recibir datos de las cabinas y almacenarlo
def datos():
    num_cabinas = 407
    resultados = []

    # Solicitar el puntaje para cada cabina
    for i in range(num_cabinas):
        while True:
            try:
                puntaje = int(input(f"Introduce el puntaje de la cabina {i + 1}: "))
                if puntaje in [2, 3, 4]:  # Verifica que el puntaje esté en el rango válido
                    break
                else:
                    print("El puntaje debe ser 2, 3 o 4. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entero.")

        clasificacion = clasificar_funcionamiento(puntaje)
        resultados.append((i + 1, puntaje, clasificacion))

    # Mostrar los resultados
    print("\nListado de resultados:")
    print(f"{'Cabina_ID':<12} {'Puntaje':<10} {'Clasificación':<30}")
    print("="*52)
    for cabina_id, puntaje, clasificacion in resultados:
        print(f"{cabina_id:<12} {puntaje:<10} {clasificacion:<30}")

# Llamar a la función directamente // vi que también se puede llamar de forma que se especifique que es esta la función que debe correr
datos()