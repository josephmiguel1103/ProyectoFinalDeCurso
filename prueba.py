from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.colors import HexColor
from cliente import Persona, buscar_persona
from cuenta import nueva_factura
w, h = A4
c = canvas.Canvas("factura.pdf", pagesize=A4)


def pruebal():
    #datos cliente y producto
    DatoCliente ,DatoProducto,cantidad,factura  = nueva_factura()
    # logo
    c.drawImage("logo.png", 25, h - 80, width=70, height=65)

    # info basica de tienda
    c.setFont("Courier-BoldOblique", 24)
    c.drawString(100, 780, "PASTELERIA PIÚDULCE")
    c.setFont("Courier-Oblique", 10)
    c.drawString(40, h - 105, "Fabricacion y venta de productos de pasteleria")
    c.setFont("Courier-Oblique", 8)
    c.drawString(67, h - 112, "tuttoBello Reposteria Piúdulce, S.A de C.V")
    c.drawString(125, h - 119, "RFC:SRF045DDFU49")
    c.drawString(95, h - 125, "pasteleriaPiúdulce@suquie.com")

    # Nro factura
    Serie =factura.serie
    c.setFont("Courier-BoldOblique", 15)
    c.drawString(420, h - 60, "FACTURA")
    c.drawString(430, h - 78, f"N° {Serie} ")
    c.roundRect(405, 750, 120, 55, 20, stroke=1)


    #DatoProducto , continua = agregarProducto()

    # datos del cliente

    nombre = DatoCliente.nombres
    direction = DatoCliente.direccion
    telephone = DatoCliente.telefono

    now = datetime.now()
    format = now.strftime(
        '%d / %m / %Y -- Hora: %H, Minutos: %M, Segundos: %S')

    c.setFont("Courier-Bold", 10)
    c.drawString(40, h - 140, f"FECHA: {format}")
    c.drawString(40, h - 150, f"CLIENTE: {nombre}")
    c.drawString(40, h - 160, f"DIRECCION: {direction} ")
    c.drawString(40, h - 170, f"TELEFONO: {telephone}")

    # datos producto
    c.setFillColor(HexColor('#f59622'))
    c.rect(40, h-180, 500, -17, fill=1, stroke=False)
    c.setFillColor(HexColor('#ffffff'))
    c.drawString(43, h - 190, "CANTIDAD ")
    c.drawString(200, h - 190, "NOMBRE ")
    c.drawString(340, h - 190, "PRECIO UNITARIO ")
    c.drawString(500, h - 190, "TOTAL  ")
    
    #datoProducto
    #cifra= factura.detalle.cantidad
    monto= factura.total
    nombreProducto=DatoProducto.nombre
    precioProducto= DatoProducto.precio
    c.setFillColor(HexColor('#303030'))
    c.drawString(43, h - 210, f" {cantidad} ")
    c.drawString(180, h - 210, f" {nombreProducto}")
    c.drawString(355, h - 210, f" {precioProducto}")
    c.drawString(500, h - 210, f" {monto} ")
    # datos de total de venta

    c.setFillColor(HexColor('#f45466'))
    c.drawString(390, h - 370, "SUBTOTAL ")
    c.drawString(390, h - 380, "IGV ")
    c.drawString(390, h - 390, "TOTAL ")

    baseImponible = factura.base_imponible
    igv =factura.igv
    total =factura.total
    c.setFillColor(HexColor('#190202'))
    c.drawString(450, h - 370, f"{baseImponible}")
    c.drawString(450, h - 380, f"{igv}")
    c.drawString(450, h - 390, f"{total}")


    c.setFont("Courier-Oblique", 10)
    c.drawString(40, h - 380, "R.U.C.N° 364324333423425")
    c.setFont("Courier-Oblique", 8)
    c.drawString(67, h - 390, "N° De autorizacion de impresion")
    c.drawString(125, h - 400, "133223244")
    c.drawString(95, h - 410, "pasteleriaPiúdulce@suquie.com")

    c.showPage()
    c.save()
