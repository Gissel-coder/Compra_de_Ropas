class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre  
        self.__precio = precio  
        self.__cantidad = cantidad  

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}, Precio: ${self.__precio}, Stock: {self.__cantidad}")

    def vender(self, cantidad):
        if cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
            print(f"Se han vendido {cantidad} de {self.__nombre}.")
        else:
            print(f"No hay suficiente stock de {self.__nombre}.")


class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  
        self.__talla = talla 

    def mostrar_info(self):
        super().mostrar_info()  
        print(f"Talla: {self.__talla}")


class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad) 
        self.__talla = talla  

    def mostrar_info(self):
        super().mostrar_info()  
        print(f"Talla: {self.__talla}")


class ZapatosHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  
        self.__talla = talla  

    def mostrar_info(self):
        super().mostrar_info() 
        print(f"Talla: {self.__talla}")


class ZapatosMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  
        self.__talla = talla  

    def mostrar_info(self):
        super().mostrar_info()  
        print(f"Talla: {self.__talla}")


class Inventario:
    def __init__(self):
        self.__prendas = []  

    def agregar_prenda(self, prenda):
        self.__prendas.append(prenda) 

    def mostrar_inventario(self):
        for prenda in self.__prendas:
            prenda.mostrar_info()  


if __name__ == "__main__":
    
    camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
    pantalon = RopaHombre("Pantalón de Hombre", 30.00, 30, "L")
    chaqueta = RopaHombre("Chaqueta de Hombre", 55.00, 20, "M")
    
    falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
    blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "M")
    vestido = RopaMujer("Vestido de Mujer", 45.00, 10, "L")
    
    zapatos_hombre = ZapatosHombre("Zapatos de Hombre", 60.00, 25, "42")
    zapatos_mujer = ZapatosMujer("Zapatos de Mujer", 50.00, 20, "37")

    # Aquí se crea el inventario y se agregar las mercaderias
    inventario = Inventario()
    inventario.agregar_prenda(camisa)
    inventario.agregar_prenda(pantalon)
    inventario.agregar_prenda(chaqueta)
    inventario.agregar_prenda(falda)
    inventario.agregar_prenda(blusa)
    inventario.agregar_prenda(vestido)
    inventario.agregar_prenda(zapatos_hombre)
    inventario.agregar_prenda(zapatos_mujer)

    # Mostramos el inventario
    print("Inventario de Ropa:")
    inventario.mostrar_inventario()

    # Se hace la compra
    camisa.vender(2)  
    pantalon.vender(5)  
    falda.vender(1)  
    blusa.vender(3) 
    zapatos_hombre.vender(1)  
    zapatos_mujer.vender(2)  

    #Inventario luego de las ventas
    print("\nInventario después de las ventas:")
    inventario.mostrar_inventario()
