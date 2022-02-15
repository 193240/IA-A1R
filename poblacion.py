
import numpy as np
from operadoresGeneticos import *
from primeraG import *
def seleccion(lista):
    padres = []
    p1=random.randint(0,len(lista)-1)
    individuo1 = lista.pop(p1)
    p2=random.randint(0,len(lista)-1)
    individuo2 = lista.pop(p2)
    padres.append(individuo1)
    padres.append(individuo2)
    return padres
def binario_decimal(binario):
    numero = int(binario,2)
    datos = [numero, binario]
    return datos

def ajuste(individuo, tamañoX,tamañoY): #valoresX, valoresY
    if(individuo["iX"]>tamañoX or individuo["iY"]>tamañoY):
        return None
    else: return individuo



def crear_individuo(intervaloX,intervaloY, arrayX, arrayY,deltaX, deltaY):
    fenotipoX = fenotipo(intervaloX[0],arrayX[0],deltaX)
    fenotipoY = fenotipo(intervaloY[0], arrayY[0], deltaY)
    aptitudT = aptitud(fenotipoX,fenotipoY)
    individuo = {
        "genotipoX": arrayX[1],
        "iX": arrayX[0],
        "fenotipoX": fenotipoX,
        "genotipoY": arrayY[1],
        "iY": arrayY[0],
        "fenotipoY": fenotipoY,
        "aptitud": aptitudT
    }
    return individuo

def prox_generacion(lista, pro_individuo, pro_genotipo, intervaloX, intervaloY, resolucion,bitsX, bitsY,cantidadX, cantidadY,deltaX,deltaY):
    familia = []
    while len(lista) != 0:
        if len(lista)==1:
            clon = lista.pop()
            familia.append(clon)
            x = mutacionI(clon['genotipoX'], pro_individuo, pro_genotipo)
            y = mutacionI(clon['genotipoY'], pro_individuo, pro_genotipo)
            nuevoClon = crear_individuo(intervaloX, intervaloY, binario_decimal(x), binario_decimal(y), deltaX, deltaY)
            familia.append(nuevoClon)
        else:
            padres = seleccion(lista)
            listaX=[]
            listaY=[]
            hijosX = cruzaX(padres[0], padres[1],bitsX, pro_individuo,pro_genotipo)
            hijosY = cruzaY(padres[0], padres[1],bitsY, pro_individuo,pro_genotipo)

            for x in hijosX:
                listaX.append(binario_decimal(x))
            for y in hijosY:
                listaY.append(binario_decimal(y))
            for i in range(2):
                individuo = crear_individuo(intervaloX, intervaloY,listaX[i],listaY[i],deltaX, deltaY)

                individuoA= ajuste(individuo,cantidadX,cantidadY)
                #print(individuoA)
                if (individuoA != None):
                    familia.append(individuoA)
                #else:
                    #print("no apto:", individuo)
            for i in padres:
                familia.append(i)

    return familia

def evolucion_fitness(lista,generacion):
    array = []
    suma = 0
    for e in lista:
        array.append(e['aptitud'])
    suma = sum(array)
    cantidad_elementos = len(lista)
    promedio = suma / cantidad_elementos
    max_value = max(array)
    min_value = np.amin(array)
    data = {
        "generacion": generacion+1,
        "peor": min_value,
        "mejor": max_value,
        "promedio": promedio
    }
    return data

def mejor_individuo(lista):
    lis=sorted(lista, key = lambda i: i['aptitud'])
    mejor = lis.pop()
    return mejor