from producto import Producto
from utils import limpiarPantalla,continuar
import time
productos: Producto = []


def productoDict():
    x : dict = [{"codigo":"12345","nombre":"pan frances","precio":0.6,"marca":"union"},\
        {"codigo":"12343","nombre":"rollo de pan","precio":1,"marca":"union" },\
            {"codigo":"23232","nombre":"maraqueta","precio":1.5,"marca":"union" },\
            {"codigo":"24433","nombre":"pastel de vainilla","precio":20,"marca":"union" },\
            {"codigo":"12643","nombre":"pastel de especies","precio":32,"marca":"union" }]
    a=0
    for i in x: 
        producto: Producto = Producto(x[a]["codigo"],x[a]["nombre"], x[a]["precio"],x[a]["marca"],)
        productos.append(producto)
        a=a+1

def producto():
    limpiarPantalla()

    print("***ingresar datos del producto ***\n")
    codigo: str = str(input("Ingrese código: "))
    nombre: str = str(input("Ingrese nombre: "))
    precio: float = float(input("Ingrese precio: "))
    marca: str = str(input("Ingrese marca: "))
    producto: Producto = Producto(codigo, nombre, precio, marca)
    productos.append(producto)

    continuar()


def listar_producto():
    limpiarPantalla()
    print("   CODIGO     NOMBRE   PRECIO    MARCA  ")
    for producto in productos:
        Producto.convertir_a_string(producto)
    continuar()


def buscar_producto():

    codigo: str = str(input("Ingrese Código para buscar el producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            time.sleep(2)
            return producto
    continuar()


def editar_producto():
    limpiarPantalla()
    codigo: str = str(input("Ingrese codigo para buscar producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            producto.nombre = str(input("Ingrese nuevo nombre: "))
            Producto.convertir_a_string(producto)
    continuar()

def eliminar_producto():
    limpiarPantalla()
    codigo: str = str(input("Ingrese codigo para buscar producto: "))
    for indice, producto in enumerate(productos):
        if producto.dni == codigo:
            productos.pop(indice)
            print("\nSe elimino correctamente el usuario")
    continuar()
