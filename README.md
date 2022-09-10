# Libreria #2 Números complejos:

_En esta libreria encontraremos el complemento de la libreria #1, donde encontraremos las siguientes operaciones:_
1. Adición de vectores complejos.
2. Inverso (aditivo) de un vector complejo.
3. Multiplicación de un escalar por un vector complejo.
4. Adición de matrices complejas.
5. Inversa (aditiva) de una matriz compleja.
6. Multiplicación de un escalar por una matriz compleja.
7. Transpuesta de una matriz/vector
8. Conjugada de una matriz/vector
9. Adjunta (daga) de una matriz/vector
10. Producto de dos matrices (de tamaños compatibles)
11. Función para calcular la "acción" de una matriz sobre un vector.
12. Producto interno de dos vectores
13. Norma de un vector
14. Distancia entre dos vectores
15. Revisar si una matriz es unitaria
16. Revisar si una matriz es Hermitiana
17. Producto tensor de dos matrices/vectores
### Pre-requisitos
_Para poder correr nuestra libreria necesitaremos un iDLE cualquiera de python._\
_Sin embargo, para esta oportunidad debemos asegurarnos de tener instaladas las librerias de math y de copy, debido a que en ocasiones algunas librerias no se encuentran instaladas por defecto con nuestro iDlE de preferencia._ \
_Además, se utilizaran las siguientes funciones auxiliares para permitir un buen funcionamiento de la libreria:_
```
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

def multiplicacionComplejos(numero1, numero2):      #3
    res = ()
    res = ((numero1[0]*numero2[0])-(numero1[1]*numero2[1]), (numero1[0]*numero2[1])+(numero2[0]*numero1[1]))
    return (res)
```
### Ejemplos
_A continuación encontraremos el ejemplo de la función donde se oberva la acción de una matriz sobre un vector:_
```
def accionMatrizVector(matriz, vector):
    vector_resultante = []
    for i in range(len(vector)):
        vector_resultante.append(0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            vector_resultante[i] += matriz[i][j]*vector[j]
    return vector_resultante
```
_¿Cómo podemos verificar estos resultados?_\
_En esta ocasión tenemos que esta acción generalmente es de manera real o de manera compleja, esta función nos da como resultado un vector ya sea con componentes reales o imaginarias._
```
vector_resultante = []
    for i in range(len(vector)):
        vector_resultante.append(0)
```
_En estas lineas de codigo vamos a generar una matriz del tamaño del vector resultante llena de 0's para que a la hora de rellenar la matriz sea más sencillo de hacer y evitar problemas a la hora de agregar elementos._
```
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            vector_resultante[i] += matriz[i][j]*vector[j]
```
_En este ciclo anidado, vamos a realizar la operación para encontrar el vector resultante, en donde multiplicamos cada componente de cada fila de la matriz por cada componente del vector dado._
### Pruebas en codigo
_Al finalizar cada función encontraremos la prueba de la misma; a continuación un ejemplo de ellas:_
```
v1 = [(1,1),(1,1)]
v2 = [(1,1),(1,1)]
sumaVectorComplejo(v1,v2)

v = [(1,1),(-2,2)]
inversoAditivo(v)

numero = 0
v1Complx = [(1,1),(1,1)]
multiplicacionEscalarVectorComplejo(numero, v1Complx)

matrizComplx1, matrizComplx2 = [[(1,1),(1,1)],[(1,1),(1,1)]], [[(1,1),(1,1)],[(1,1),(1,1)]]
adicionMatricesComplejas(matrizComplx1, matrizComplx2)

matrizComplx1 = [[(1, -2), (1, -2)], [(1, -2), (1, -2)]]
inversaAditivaMatrizCompleja(matrizComplx1)

numero = 2
matriz = [[(1,1),(1,1)],[(1,1),(1,1)],[(1,1),(1,1)]]
multiplicacionEscalarMatrizCompleja(numero, matriz)

matriz = [[1,2],[1,2]]
transpuestaMatriz(matriz)

matrizComplx1 = [[(5,0),(4,5),(6,-16)],[(4,-5),(13,0),(7,0)],[(6,16),(7,0),(-2.1,0)]]
conjugadaMatriz(matrizComplx1)

matrizComplx1 = [[(1,2),(1,3)],[(1,5),(1,6)]]
adjuntaMatriz(matrizComplx1)

matriz = [[(2,2),(2,2)],[(2,2),(2,2)]]
matriz1 = [[(2,2),(2,2)],[(2,2),(2,2)]]
productoMatrices(matriz, matriz1)

matriz = [[0,0,1,1],[0,0,1,-1],[1,1,0,0],[1,-1,0,0]]
vector =[0,0,0,1]
accionMatrizVector(matriz, vector)

v1, v2 = [1,2],[1,2]
productoInternoVectores(v1, v2)

v1 = [1,2]
normaVector(v1)

v1, v2 = [1,2],[1,2]
distanciaVectores(v1, v2)

matriz = [[(1/math.sqrt(2), 0),(1/math.sqrt(2), 0)],[(1/math.sqrt(2), 0),(-1/math.sqrt(2), 0)]]
esMatrizUnitaria(matriz)

hermitiana = [[(5,0),(4,5),(6,-16)],[(4,-5),(13,0),(7,0)],[(6,16),(7,0),(-2.1,0)]]
esMatrizHermitiana(hermitiana)

matriz = [[1,1],[1,1]],[[1,1],[1,1]]
productoTensor(matriz)
```
_Estas lineas prueban una a una cada función con sus respectivas variables dependiendo el parametro de cada función a ensayar._

## ¿Como lo construimos?
* [Pycharm](https://www.jetbrains.com/es-es/pycharm/) -_El iDLE usado_

## Autor
* **Oscar Lesmes** - *Libreria completa* - [GitHub](https://github.com/villanuevand)

