class Operaciones(object):

    def creacionDiccionario(listaCadaveres):
        listaCadaveres2 = {}
        listaCadaveresA = []
        listaCadaveresB = []
        listaCadaveresC = []
        listaCadaveresD = []
        listaCadaveresE = []
        listaCadaveresF = []
        listaCadaveresG = []
        listaCadaveresH = []
        listaCadaveresI = []
        listaCadaveresJ = []
        listaCadaveresK = []
        listaCadaveresL = []
        for l in listaCadaveres:
            listaCadaveresA.append(l[0])
            listaCadaveresB.append(l[1])
            listaCadaveresC.append(l[2])
            listaCadaveresD.append(l[3])
            listaCadaveresE.append(l[4])
            listaCadaveresF.append(l[5])
            listaCadaveresG.append(l[6])
            listaCadaveresH.append(l[7])
            if(l[8] == ""):  # Dado que hay valores desconocidos se convierten en 0 para su estudio
                l[8] = "0"
            listaCadaveresI.append(l[8])  # Se convierten los valores a enteros
            listaCadaveresJ.append(l[9])
            listaCadaveresK.append(l[10])
            l[11] = l[11].replace("\n", "")
            l[11] = l[11].replace(",", "")
            listaCadaveresL.append(l[11])
        listaCadaveres2['Zona'] = listaCadaveresA
        listaCadaveres2['Provincia'] = listaCadaveresB
        listaCadaveres2['Canton'] = listaCadaveresC
        listaCadaveres2['Distrito'] = listaCadaveresD
        listaCadaveres2['Circuito'] = listaCadaveresE
        listaCadaveres2['Fecha'] = listaCadaveresF
        listaCadaveres2['Hora'] = listaCadaveresG
        listaCadaveres2['Tipo de Muerte'] = listaCadaveresH
        listaCadaveres2['Edad'] = listaCadaveresI
        listaCadaveres2['Sexo'] = listaCadaveresJ
        listaCadaveres2['Estado Civil'] = listaCadaveresK
        listaCadaveres2['Nacionalidad'] = listaCadaveresL
        return listaCadaveres2
