# def listaNumeros(inicio,fin,salto):
#     print(list(range(inicio,fin,salto)))

# listaNumeros(10, 20, 2)
# listaNumeros(20, 30, 2)

# def aprender_a_programar():
#     print("Puedes aprender a programar gratis en freeCodeCamp")

#     def aprender_que_lenguaje():
#         print("Puedes aprender cualquier lenguaje de programación en el canal de YouTube de freeCodeCamp")
    
#     aprender_que_lenguaje()

# aprender_a_programar()

def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total
print (suma([1,3,5,4])) # 13