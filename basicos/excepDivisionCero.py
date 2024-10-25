num1 = int(input("introduce un numero: "))
num2 = int(input("introduce otro numero: "))
try:
    print(f"La division de {num1} entre {num2} es {num1/num2}")
except ZeroDivisionError:
    print("Controlo un error al dividir por cero")
