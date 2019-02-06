# from bokeh.plotting import figure, output_file, show
from ManejodeArchivos.Manejo import LecturaArchivo as la
from ManejodeArchivos.Manejo import crearArchivo as ca


cuerpos = la("Documentos/metadatos-homicidios-asesinatos--20142.csv")
cadaveres = ca("Documentos/levantamientoCadaveres.csv")
ListaZona = []
listaCadaveres = cuerpos.leerInformacion()
listaCadaveres = [l.replace(";", ",") for l in listaCadaveres]
for l in listaCadaveres:
    print(l)
    cadaveres.agregarInformacion(l)
