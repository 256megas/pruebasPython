# https://www.youtube.com/watch?v=9x7RK6mb1uA

class Coche:
    def __init__(self, marca, modelo):
        # dunder=double underscore
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print(f"El {self.marca},{self.modelo} ha sido arrancado")

    def parar(self):
        self.arrancado = False
        print(f"El {self.marca},{self.modelo} se ha parado")


laguna = Coche("Renault", "Laguna")
tesla = Coche("Tesla", "Model 3")

print(type(laguna))
print(type(tesla))
print(laguna.marca, laguna.modelo)
print(tesla.marca, tesla.modelo)
print(laguna.arrancado)
laguna.arrancar()
print(laguna.arrancado)
laguna.parar()
print(laguna.arrancado)
