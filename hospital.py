def clasificar_diagnostico(puntaje):
    #Clasifica el nivel de leucemia basado en el puntaje.
    if puntaje < 10:
        return "No tiene Leucemia"
    elif 11 <= puntaje <= 40:
        return "Nivel Bajo de Leucemia"
    elif 41 <= puntaje <= 69:
        return "Nivel Moderado de Leucemia"
    elif 70 <= puntaje <= 100:
        return "Nivel Grave de Leucemia"
    else:
        return "Puntaje fuera del rango esperado"

def diagnostico():
    num_pacientes = 803
    resultados = []

    # Solicitar el puntaje para cada paciente
    for i in range(num_pacientes):
        while True:
            try:
                puntaje = int(input(f"Introduce el puntaje del paciente {i + 1}: "))
                if 0 <= puntaje <= 100:  # Verificar que el puntaje esté en un rango válido
                    break
                else:
                    print("El puntaje debe estar entre 0 y 100. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entero.")

        clasificacion = clasificar_diagnostico(puntaje)
        resultados.append((i + 1, puntaje, clasificacion))

    # Mostrar los resultados
    print("\nListado de resultados:")
    print(f"{'Paciente_ID':<12} {'Puntaje':<10} {'Clasificación':<30}")
    print("="*52)
    for paciente_id, puntaje, clasificacion in resultados:
        print(f"{paciente_id:<12} {puntaje:<10} {clasificacion:<30}")

# Llamar a la función directamente
diagnostico()