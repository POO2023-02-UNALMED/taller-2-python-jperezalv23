class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro 
    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color

    
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro 
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo


class Auto:
    numinstancias = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        Auto.numinstancias += 1
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = Auto.numinstancias

    def cantidadAsientos(self):
        cantidadasientos = 0
        for i in range(len(self.asientos)):
            if self.asientos[i] != None:
                cantidadasientos += 1
        return cantidadasientos
    
    def verificarIntegridad(self):
        if self.motor.registro == self.registro:
            for i in range(len(self.asientos)):
                if self.asientos[i].registro != self.registro:
                    return "Las piezas no son originales"
                else: "Auto original"
        else: 
            return "Las piezas no son originales"

    
    


        