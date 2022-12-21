import os


def limpiarPantalla():
    os.system("cls")

def continuar():
    seguir= str(input("\n>>> continuar? s/n: "))
    if seguir == "si" or seguir == "SI" or seguir=="":
        limpiarPantalla()
    else :
        continuar()