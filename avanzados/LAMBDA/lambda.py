lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

filtrado = list(filter(lambda x: x % 2 == 0, lista))
# Map recorre todo
# Filter filtra contenido
# Reduce acumula
print(filtrado)
