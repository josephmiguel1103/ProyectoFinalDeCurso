from cliente import Persona,buscar_persona
from cartaProducto import Producto,buscar_producto
from factura import Factura
from factura_detalle import FacturaDetalle
from utils import continuar
import time

facturas: Factura = []

def nueva_factura():
    print("para generar una factura busca un cliente")
    time.sleep(1)
    cliente: Persona = buscar_persona()
    factura: Factura = Factura(len(facturas)+1, cliente)
    continua: bool = True

    while continua:

        producto: Producto = buscar_producto()
        cantidad: int = int(input("Ingrese la cantidad: "))
        print("  CODIGO     PRODUCTO   PRECIO  BASE INPONIBLE    IGV   CANTIDAD    TOTAL   ")
        factura.detalle.append(FacturaDetalle(
            producto.codigo, producto.nombre, cantidad, producto.precio))
        
        #agregarProducto(producto,continua)

        condicion: str = str(input("SI para agregar mas productos: "))

        if condicion == "SI" or condicion == "si":
            continua = True
        else:
            continua = False
            factura.calcular_igv()
            facturas.append(factura) 
            continuar()
    
    return cliente,producto,cantidad,factura


def listar_factura():
    print(" SERIE Nr°   DNI   NOMBRE  BASE INPONIBLE    IGV   TOTAL\n ")
    for factura in facturas:
        Factura.convertir_a_string(factura)
    continuar()

def buscar_factura():
    numero:int=int(input("Ingrese el numero de la factura: "))
    for factura in facturas:
        if factura.numero==numero:
            Factura.convertir_a_string(factura)
            print("===========================")
            print("  CODIGO     PRODUCTO   PRECIO  BASE INPONIBLE    IGV   CANTIDAD    TOTAL   ")
            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)
        continuar()