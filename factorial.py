def calculaFactorial(valor):
    resultado: int = 1
    for i in range(2, valor+1):
        # print (i)
        resultado = resultado * i
    # print ("+++++")
    print(f"El favtorial de {valor} es {resultado}")


valor: int = 1
while (valor != 0):
    print("Si introduces 0 el programa deberia de salir")
    valor = int(input("introduce un numero: "))
    calculaFactorial(valor)
