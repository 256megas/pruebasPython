from datetime import datetime


class Persona:
    nombre: str
    edad: int
    altura: float
    peso: float
    genero: str
    caminando: bool

    def __init__(self, nombre, edad, altura, peso, genero):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.caminando = False

    def toString(self):
        print("Nombre: ", self.nombre)
        print("Edod: ", self.edad)
        print("Altura: ", self.altura)
        print("Peso: ", self.peso)
        print("Genero: ", self.genero)
        if (self.caminando):
            print("Esta caminando")
        else:
            print("Esta quieto")
        print("IMC: ", self.imc())

    def imc(self):
        return (round(self.peso/(self.altura**2), 2))

    def andar(self):
        self.caminando = True

    def parar(self):
        self.caminando = False

    @classmethod
    def calcularEdad(cls, ano):
        anoActual = int(datetime.now().strftime('%Y'))
        print(f"Si naciste en el año {ano} tienes {anoActual-ano}")


persona = Persona("Flipendo", 30, 1.80, 70.4, "hombre")

persona.toString()

Persona.calcularEdad(1986)
