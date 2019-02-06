import codecs as cdc


class LecturaArchivo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = cdc.open(self.nombre, "r")

    def leerInformacion(self):
        return self.archivo.readlines()

    def cerrarArchivo(self):
        self.archivo.close()


class crearArchivo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = cdc.open(self.nombre, "a")

    def agregarInformacion(self, l):
        self.archivo.write(l)
