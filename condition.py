try:
    valor: int = 1
    while (valor != 0):
        print("Si introduces 0 el programa deberia de salir")
        valor = int(input("introduce un numero: "))
        if (valor == 0):
            print("ADIOS")
            # print(f"El numero {valor} es cero")
            break
        elif (valor % 2 == 0):
            print(f"El numero {valor} es par")
        elif (valor % 2 != 0):
            print(f"El numero {valor} es impar")
        print("++++++++++++++++++++++++++++++++++++++++++")

except:
    print("Has introducido algo que no es un número")
