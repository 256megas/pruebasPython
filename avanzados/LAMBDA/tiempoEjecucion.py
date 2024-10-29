from datetime import datetime


def tiempoEjecucion(funcion):
    def wrapper(*args, **kargs):
        inicio = datetime.now()
        print(f"Empieza la ejecucion a {inicio}")
        resultado = funcion()
        fin = datetime.now()
        print(f"Acaba la ejecucion a {fin}")
        tiempoEjec = fin-inicio
        print(f"Se ejecuta en {tiempoEjec}")
        return resultado
    return wrapper


@tiempoEjecucion
def desarrollo():
    for x in range(10):
        print(f"Procesamos el número {x}")
    print(datetime.now())


desarrollo()
