# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:57:39 2022
@author: Oscar Lesmes
"""
import math
##FUNCIONES AUXILIARES
def sumaComplejos(numero1, numero2):
    res = ()
    sumaReal = numero1[0] + numero2[0]
    sumaImaginaria = numero1[1] + numero2[1]
    res = (sumaReal, sumaImaginaria)
    return (res)

def multiplicacionEscalarAComplejo(numero, c1):
    res = ()
    res += ((numero * c1[0]),(numero * c1[1]))
    return res

def conjugadoComplejo(numero1):
    conjugadoImaginario = numero1[1] * -1
    res = (numero1[0], conjugadoImaginario)
    return (res)
###################################################

##Adición de vectores complejos.                                           #1
def sumaVectorComplejo(v1, v2):
    res = []
    for i in range(len(v1)):
        res += [sumaComplejos(v1[i], v2[i])]
    for i in range(len(res)):
        return (res[i])
v1 = [(1,1),(1,1)]
v2 = [(1,1),(1,1)]
sumaVectorComplejo(v1,v2)

##Inverso (aditivo) de un vector complejo.                                   #2
def inversoAditivo(v):
    matriz_f = []
    for i in range(len(v)):
        matriz_f.append(multiplicacionEscalarAComplejo(-1, v[i]))
    return matriz_f

v = [(1,1),(-2,2)]
inversoAditivo(v)

##Multiplicación de un escalar por un vector complejo.                        #3
def multiplicacionEscalarVectorComplejo(numero, v1Complx):
    vector = []
    for i in range(len(v1Complx)):
        vector += [multiplicacionEscalarAComplejo(numero, v1Complx[i])]
    return vector

numero = 0
v1Complx = [(1,1),(1,1)]
multiplicacionEscalarVectorComplejo(numero, v1Complx)

##Adición de matrices complejas.                                                #4
def adicionMatricesComplejas(matrizComplx1, matrizComplx2):
    matriz_f = []
    for i in range (len(matrizComplx1)):
        matriz_f.append([0]*len(matrizComplx2[i]))
    for i in range (len(matrizComplx1)):
        for k in range (len(matrizComplx1)):
            matriz_f[i][k] = sumaComplejos(matrizComplx1[i][k], matrizComplx2[i][k])
    return matriz_f
matrizComplx1, matrizComplx2 = [[(1,1),(1,1)],[(1,1),(1,1)]], [[(1,1),(1,1)],[(1,1),(1,1)]]
adicionMatricesComplejas(matrizComplx1, matrizComplx2)


##Inversa (aditiva) de una matriz compleja.                                       #5
def inversaAditivaMatrizCompleja(matrizComplx1):
    matriz_f = []
    for i in range (len(matrizComplx1)):
        matriz_f.append([0]*len(matrizComplx1[i]))

    for i in range(len(matrizComplx1)):
        for k in range(len(matrizComplx1[i])):
            matriz_f [i][k] = multiplicacionEscalarAComplejo(-1, matrizComplx1[i][k])
    return matriz_f

matrizComplx1 = [[(1, -2), (1, -2)], [(1, -2), (1, -2)]]
inversaAditivaMatrizCompleja(matrizComplx1)

##Multiplicación de un escalar por una matriz compleja.                           #6
def multiplicacionEscalarMatrizCompleja(numero, matriz):
    matriz_f = []
    for i in range(len(matriz)):
        matriz_f.append([0]*len(matriz[i]))
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            matriz[i][k] = multiplicacionEscalarAComplejo(numero, matriz[i][k])
    return matriz
numero = 2
matriz = [[(1,1),(1,1)],[(1,1),(1,1)],[(1,1),(1,1)]]
multiplicacionEscalarMatrizCompleja(numero, matriz)

##Transpuesta de una matriz/vector                                               #7
def traspuestaMatriz(matriz):
    objeto = " "
    for i in range(len(matriz)):
        for k in range(i,len(matriz)):
            objeto = matriz[k][i]
            matriz[k][i] = matriz[i][k]
            matriz[i][k] = objeto
    return matriz

##Conjugada de una matriz/vector                                                #8
def conjugadaMatriz(matrizComplex1):
    matriz_f = []
    for i in range(len(matrizComplx1)):
        matriz_f.append([0] * len(matrizComplx1[i]))

    for i in range(len(matrizComplex1)):
        for k in range(len(matrizComplex1[i])):
            matriz_f[i][k] = conjugadoComplejo(matrizComplex1[i][k])
    return matriz_f
matrizComplx1 = [[(1,1),(1,1)],[(1,1),(1,1)]]
conjugadaMatriz(matrizComplx1)

##Adjunta (daga) de una matriz/vector                                           #9
def adjuntaMatriz(matrizComplx1):
    matrizF = conjugadaMatriz(matrizComplx1)
    res = traspuestaMatriz(matrizF)
    return res
matrizComplx1 = [[(1,2),(1,3)],[(1,5),(1,6)]]
adjuntaMatriz(matrizComplx1)

##Producto de dos matrices (de tamaños compatibles)                              #10
def productoMatrices(lines, lines1):
    matriz_0 = []
    for i in range(len(lines)):
        matriz_0.append([0]*len(matriz[i]))
    for i in range(0, len(lines)):
        for k in range(0, len(matriz)):
            for j in range(0, len(matriz)):
                matriz_0[i][k] += matriz[i][j] * matriz1[j][k]
    return matriz_0

matriz = [[2,2],[2,2]]
matriz1 = [[2,2],[2,2]]
productoMatrices(matriz, matriz1)

##Función para calcular la "acción" de una matriz sobre un vector.               #11
#def accionMatrizVector():





##Producto interno de dos vectores                                               #12
def productoInternoVectores(v1, v2):
    productoInterno = 0
    for i in range(len(v1)):
        productoInterno += v1[i] * v2[i]
    return productoInterno

v1, v2 = [1,2],[1,2]
productoInternoVectores(v1, v2)

##Norma de un vector                                                            #13
def normaVector(v1):
    producto = 0
    for i in range(v1):
        producto += v1[i] ** 2
    res = math.sqrt(producto)
    return res

v1 = [1,2]
normaVector(v1)

##Distancia entre dos vectores                                                  #14
def distanciaVectores(v1, v2):
    producto = productoInternoVectores(v1,v2)
    res = math.sqrt(producto)
    return res

v1, v2 = [1,2],[1,2]
distanciaVectores(v1, v2)

##Revisar si una matriz es unitaria                                            #15
#def esMatrizUnitaria():



##Revisar si una matriz es Hermitiana                                          #16
#def esMatrizHermitiana():





##Producto tensor de dos matrices/vectores                                      #17
#def productoTensor():

