# def funcion():
#     return 5


# def generador():
#     yield 5


# print(funcion())
# # devuelve 5
# print(generador())
# # devuelve un gerador
# print("XXXXXX")

# a = generador()
# print(a)
# print(next(a))
# print(next(a))
# print("XXXXXX")

def generador2():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n


b = generador2()
print("XXXXXX")
print(b)
print(next(b))
print(next(b))
print(next(b))
# print(next(b)) #StopIteration
