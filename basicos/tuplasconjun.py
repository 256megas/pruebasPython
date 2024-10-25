# tuplas
# tupla = ("La tierra es plana?", True, False)

# print(tupla)
# print(tupla.count(True))
# print(tupla.index(False))


# conjuntos
# print(set([5, 2, 5, 1, 1.5]))
# print(set((5, 2, 5, 1, 1.5)))
# print(set(("52511.5")))

# conjunto = set([2, 3, 3, 4])
# print(conjunto)
# conjunto.add(1)
# print(conjunto)

# conjunto2 = set([5, 3, 5, 6])
# conjunto3 = set([4, 2])
# print(conjunto, conjunto2, conjunto3)
# print(conjunto.intersection(conjunto3))
# print(conjunto3.issubset(conjunto))
# print(conjunto3 & conjunto)

# Diccionarios
# diccionario = {1: "Uno", 2: "Dos"}
# print(diccionario)
# diccionario2 = dict({1: "Uno", 2: "Dos"})
# print(diccionario, diccionario.keys(),
#       diccionario.values(), diccionario.items())


# Ejercicio
list = [0, 1, 1, 2, 3, 5, 5, 8, 13, 21, 34, 34, 25]
print(list)
conjunto = set(list)
print(conjunto)
resultado = []
for i in conjunto:
    resultado.append(i)
print(f"El resultado es {resultado}")
