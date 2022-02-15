import random

import numpy.random



'''def cruza(genotipoX,genotipoY,pro_cruza):
    hijo1 = genotipoX.copy()
    hijo2 = genotipoY.copy()
    if rand() < pro_cruza:
        # select crossover point that is not on the end of the string
        pt = random.randint(1, len(hijo1) - 2)
        # perform crossover
        c1 = hijo1[:pt] + hijo2[pt:]
        c2 = hijo2[:pt] + hijo1[pt:]
    return [c1, c2]'''
def cruza_clon(clon, bitsX,pro_individuo,pro_genotipo):
    listaX= []
    #values = padre1.values()
    x = clon['genotipoX']#0101010101
    y = clon['genotipoY']#01010010101
    cruzaX = random.randint(1,bitsX)
    nuevoX = mutacionI(x, pro_individuo, pro_genotipo)
    nuevoY = mutacionI(y, pro_individuo, pro_genotipo)
    listaX.append(nuevoX)
    listaX.append(nuevoY)
    return listaX
def cruzaX(padre1,padre2, bitsX,pro_individuo,pro_genotipo):
    listaX= []
    #values = padre1.values()
    eX1 = padre1['genotipoX']#0101010101
    eX2 = padre2['genotipoX']#01010010101
    cruzaX = random.randint(1,bitsX)

    cabezaX1 = eX1[0:cruzaX]
    cabezaX2 = eX2[0:cruzaX]
    cuerpoX1 = eX1[cruzaX:bitsX]
    cuerpoX2 = eX2[cruzaX:bitsX]
    cadena1 = cabezaX1+cuerpoX2
    cadena2 = cabezaX2+cuerpoX1
    nuevoX = mutacionI(cadena1, pro_individuo, pro_genotipo)
    nuevoX2 = mutacionI(cadena2, pro_individuo, pro_genotipo)
    listaX.append(nuevoX)
    listaX.append(nuevoX2)
    return listaX


def cruzaY(padre1, padre2, bitsY, pro_individuo, pro_genotipo):
   listaY = []
   eY1 = padre1["genotipoY"]
   eY2 = padre2["genotipoY"]
   cruzaY = numpy.random.randint(1,bitsY)

   cabezaY1 = eY1[0:cruzaY]
   cabezaY2 = eY2[0:cruzaY]
   cuerpoY1 = eY1[cruzaY:bitsY]
   cuerpoY2 = eY2[cruzaY:bitsY]

   nuevoGenotipo1 = cabezaY1+cuerpoY2
   nuevoGenotipo2 = cabezaY2+cuerpoY1
   nuevoY = mutacionI(nuevoGenotipo1, pro_individuo,pro_genotipo)
   nuevoY2 = mutacionI(nuevoGenotipo2, pro_individuo,pro_genotipo)
   listaY.append(nuevoY)
   listaY.append(nuevoY2)
   return listaY



def mutacionI(aux1, pro_individo,pro_genotipo):
    nuevoG= ""
    a1 = random.uniform(0, 1)
    if (a1 <= pro_individo):
        nuevoG= mutacionG(aux1,pro_genotipo)
    else:
        nuevoG = aux1
    return nuevoG

def mutacionG(variable,pro_genotipo):
    nuevoG = ""
    for elemento in variable:
        g = random.uniform(0,1)
        if g <= pro_genotipo:
            if elemento == "0":
                elemento = "1"
            else:
                elemento= "0"
        nuevoG = nuevoG + elemento
    return nuevoG

def poda(lista, poblacionMaxima):
    lis=sorted(lista, key = lambda i: i['aptitud'])
    diferencia = len(lista) - poblacionMaxima
    #for i in range(diferencia):
    bandera = 0
    while bandera<diferencia:
        #print("poda:",lis.pop(bandera))
        lis.pop(bandera)
        bandera= bandera+1
    return lis

