from getpass import getpass
from utils import limpiarPantalla
from cliente import persona, listar_personas, buscar_persona, editar_persona, eliminar_persona,clienteDict
from cartaProducto import producto,listar_producto,buscar_producto,editar_producto,eliminar_producto,productoDict
from cuenta import nueva_factura,listar_factura,buscar_factura
import time
from prueba import pruebal
def main():

    limpiarPantalla()

    usuario = str(input("INGRESE USUARIO: "))
    contraseña = getpass("INGRESE CONTRASEÑA: ")
    if usuario == "admin" and contraseña == "contraseña":
        menuPrincipal()
    else:
        print("\nusuario o contraseña incorrecta \n ingrese otra ves los datos ")
        time.sleep(1)
        main()


def menuPrincipal():

    limpiarPantalla()

    print("***************************")
    print("    *** PASTELERIA ****    ")
    print("***********MENU************")
    print("  -> 1 CARTA CLIENTE")
    print("  -> 2 CARTA PRODUCTO")
    print("  -> 3 FACTURA ")
    print("  -> 4 Salir  ")

    print("\n ingrese una opcion ")
    opcion = str(input(">>> "))
    match opcion:
        case "1":
            cartaCliente()
        case "2":
            cartaProducto()
        case "3":
            cartaFactura()
        case "4":
            print(">>> saliendo del sistema..")
            exit()
        case _:
            print(">>> error")
            menuPrincipal()


def cartaCliente():

    while True:
        limpiarPantalla()

        print("***************************")
        print("   ***CARTA CLIENTE****   ")
        print("***********MENU************")
        print("  -> 0 AGREGAR LISTA CLIENTE")
        print("  -> 1 INGRESAR CLIENTE")
        print("  -> 2 LISTAR CLIENTES")
        print("  -> 3 BUSCAR CLIENTES")
        print("  -> 4 EDITAR CLIENTE")
        print("  -> 5 ELIMINAR CLIENTE")
        print("  -> 6 MENU PRINCIPAL")

        print("\n ingrese una opcion ")
        opcion = str(input(">>> "))
        limpiarPantalla()
        match opcion:
            case "0":
                clienteDict()
            case "1":
                persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                
                menuPrincipal()
            case _:
                print(">>> error")
                cartaCliente()


def cartaProducto():

    while True:
        limpiarPantalla()
        print("***************************")
        print("   ***CARTA PRODUCTO****   ")
        print("***********MENU************")
        print("  -> 0 AGREGAR LISTA PRODUCTO")
        print("  -> 1 INGRESAR PRODUCTO")
        print("  -> 2 LISTAR PRODUCTOS")
        print("  -> 3 BUSCAR PRODUCTO")
        print("  -> 4 EDITAR PRODUCTO")
        print("  -> 5 ELIMINAR PRODUCTO")
        print("  -> 6 MENU PRINCIPAL")

        print("\n ingrese una opcion ")
        opcion = str(input(">>> "))
        match opcion:
            case "0":
                productoDict()
            case "1":
                producto()
            case "2":
                listar_producto()
            case "3":
                buscar_producto()
            case "4":
                editar_producto()
            case "5":
                eliminar_producto()
            case "6":
                menuPrincipal()
            case _:
                print(">>> error")
                cartaCliente()

def cartaFactura():

    while True:
        limpiarPantalla()
        print("***************************")
        print("   ***   FACTURA    ****   ")
        print("***********MENU************")
        print("  -> 1 NUEVA FACTURA")
        print("  -> 2 LISTAR FACTURA")
        print("  -> 3 BUSCAR FACTURA")
        print("  -> 6 MENU PRINCIPAL")

        print("\n ingrese una opcion ")
        opcion = str(input(">>> "))
        match opcion:
            case "1":
                pruebal()
            case "2":
                listar_factura()
            case "3":
                buscar_factura()
            case "4":
                pruebal()
            case "5":
                eliminar_producto()
            case "6": 
                menuPrincipal()
            case _:
                print(">>> error")
                cartaCliente()



if __name__ == '__main__':
    main()
