# Inicializar la serie con los primeros dos números
serie = [5, 8]

# Calculamos más números en la serie hasta que tengamos al menos 100 números
while len(serie) < 120:  # 120 es un valor al azar mayor que 100 para asegurar que al omitir el num 13, hayan 100 num válidos
    siguiente_numero = serie[-1] + serie[-2]
    serie.append(siguiente_numero)

# Filtrar el número 13 y mantener solo los primeros 100 números válidos
serie_filtrada = [num for num in serie if num != 13][:100]

# Mostrar la lista de números generados
print(serie_filtrada)
print(len(serie_filtrada)) # Aquí quería corroborar que si fuesen 100 números