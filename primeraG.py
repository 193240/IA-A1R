import random
import numpy.random
from numpy.random import rand
def tamañoIntervalo(array):#calcula tamaño de los intervalos
    a = array[0]
    b= array[1]
    tamañoI = b - (a);
    return tamañoI

def cantidadValores(resolucion, tamañoI):#usa presision y tamaño de intervalo
    valores = int((tamañoI/resolucion)+1)
    return valores

def cantidadBits(valores):# metodo para calcular cantidad de bits
    bits = 1
    while True:
        if(pow(2,bits)>= valores):
            break
        bits= bits +1
    return bits

def valorDelta(tamañoI, bits):
    delta = tamañoI / pow(2,bits)
    return delta

def numerosAleatorios(bits,valores):
    datos=[]
    numero = numpy.random.randint(1, valores)
    binary = format(numero, "b").zfill(bits)
    datos.append(numero)
    datos.append(binary)
    return datos

def fenotipo(a, i , delta):#resive a de un intervalo (a,b), decimal, delta
    fenotipo = a + (i * delta)
    return fenotipo

def aptitud(fenotipoX, fenotipoY):
    aptitud = fenotipoX ** 2 - 2 * fenotipoY ** 2
    return aptitud

def primeraGen(resolucion, poblacionI, intervaloX=[], intervaloY=[]):
    list = []
    tamañoX = tamañoIntervalo(intervaloX)
    tamañoY = tamañoIntervalo(intervaloY)
    cantidadX = cantidadValores(resolucion,tamañoX)
    cantidadY = cantidadValores(resolucion, tamañoY)
    bitsX = cantidadBits(cantidadX)
    bitsY = cantidadBits(cantidadY)
    deltaX = valorDelta(tamañoX, bitsX)
    deltaY = valorDelta(tamañoY, bitsY)

    for i in range(poblacionI):
        listaX = numerosAleatorios(bitsX,cantidadX)
        listaY = numerosAleatorios(bitsY, cantidadY)
        fenotipoX = fenotipo(intervaloX[0],listaX[0],deltaX)
        fenotipoY = fenotipo(intervaloY[0],listaY[0],deltaY)
        individuo = {
            "genotipoX": listaX[1],
            "iX": listaX[0],
            "fenotipoX": fenotipoX,
            "genotipoY": listaY[1],
            "iY": listaY[0],
            "fenotipoY": fenotipoY,
            "aptitud": aptitud(fenotipoX,fenotipoY)
        }
        list.append(individuo)
    return list