lista = []
for i in range(30):
    lista.append(i)
print(lista)
# print(sorted(lista, reverse=True))
print("++++++++++++++++++++++++++++")
for i in lista:
    if (i != 0 and i % 2 == 0):
        print(i)
