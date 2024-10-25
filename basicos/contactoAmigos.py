opciones: int = 1
agenda = {}
while (opciones != 0):
    print("------------------------------------------------")
    print("OPCIONES:")
    print("1 -> MOSTRAR AGENDA ")
    print("2 -> CREAR CONTACTO")
    print("3 -> BORRAR CONTACTO")
    print("0 -> SALIR")
    try:
        opciones = int(input("Introduce una opcion: ").capitalize())
    except:
        print("Has introducido algo que no es un número")
    # calculaFactorial(opciones)
    print("------------------------------------------------")

    match opciones:
        case 1:
            print("1 -> MOSTRAR AGENDA ")
            for clave, valor in agenda.items():
                print(f"El contacto {clave} contiene el telefono {valor}")
        case 2:
            print("2 -> CREAR CONTACTO")
            nuevoContacto = str(input("Introduce el nombre de contacto: "))
            nuevoTelefono = str(input("Introduce el telefono del contacto: "))
            # Pongo el telefono como str porque no se van a hacer calculos con el
            agenda.update({nuevoContacto: nuevoTelefono})
        case 3:
            print("3 -> BORRAR CONTACTO")
            borrarContacto = str(input("Introduce el nombre de contacto: "))
            try:
                agenda.pop(borrarContacto)
                print(f"Se va a borrar el contacto {borrarContacto}")
            except:
                print("Ha habido un problema, seguramente ese contacto no exista")
        case 0:
            print("0 -> SALIR")
        case _:
            print("ESA OPCION NO ESTA IMPLEMENTADA")
    # print("------------------------------------------------")
    # print(f"La agenda tiene como resultado {agenda}")
    # print("------------------------------------------------")
