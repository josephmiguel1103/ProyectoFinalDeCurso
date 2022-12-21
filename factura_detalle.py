class FacturaDetalle:
    """ Clase que construye el detalle de una factura """

    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo:str = codigo
        self.nombre:str = nombre
        self.cantidad:float = cantidad
        self.precio:float = precio
        self.base_imponible:float = round((self.precio*self.cantidad)/1.18,2)
        self.igv:float = round((self.precio*self.cantidad)-self.base_imponible,2)
        self.total:float = round(self.precio*self.cantidad,2)
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print("| {} | {} | {} | {} | {} | {} | {} |".format(self.codigo, self.nombre, self.precio, self.base_imponible, self.igv, self.cantidad, self.total))
