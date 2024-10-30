def generadorPrimos(cantidad):
    for j in range(cantidad):
        if (esPrimo(j)):
            print(j)


def esPrimo(n):
    for i in range(2, n+1):
        if (n % i == 0 and n != i):
            return False
        return True


generadorPrimos(15)
