from datetime import datetime


class Persona:

    def __init__(self, nombre, edad, altura, peso, genero):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__peso = peso
        self.__genero = genero
        self.__caminando = False

    def toString(self):
        print("Nombre: ", self.__nombre)
        print("Edod:   ", self.__edad)
        print("Altura: ", self.__altura)
        print("Peso:   ", self.__peso)
        print("Genero: ", self.__genero)
        if (self.__caminando):
            print("Esta caminando")
        else:
            print("Esta quieto")
        print("IMC:    ", self.imc())

    def imc(self):
        return (round(self.__peso/(self.__altura**2), 2))

    def andar(self):
        self.__caminando = True

    def parar(self):
        self.__caminando = False

    @classmethod
    def calcularEdad(cls, ano):
        anoActual = int(datetime.now().strftime('%Y'))
        print(f"Si naciste en el año {ano} tienes {anoActual-ano}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, altura, peso, genero, tiempoEstudioDiario):
        super().__init__(nombre, edad, altura, peso, genero)
        self.__tiempoEstudioDiario = tiempoEstudioDiario

    def toString(self):
        super().toString()
        print("Estudia:", self.__tiempoEstudioDiario)


persona = Persona("Mortadelo", 38, 1.80, 100.4, "hombre")

persona.toString()

Persona.calcularEdad(1986)
print("*******************************************")
estudiante = Estudiante("Filemona", 35, 1.65, 65.4, "mujer", 180)
estudiante.toString()
