# 2021-S1-portafolio3

El archivo debe llamarse **portafolio3.py**, además respetar el nombre de las funciones que más adelante se describen

## construir
Construir una función que forme un número a partir de otro, considerando sólo los dígitos pares del número de entrada.

```python
>>>construir(2345)     
24
```
## digitoMenor
Construir una función  que reciba un número entero y retorne el dígito menor.
```python
>>>digitoMenor(569803)      
0
```
## digitosOrdenados
Construir una función que reciba un número e indique si sus dígitos están ordenados de manera descendente.
```python
>>>digitosOrdenados(2345678)   
True
```
## elevarNumero
Construir una función que eleve un número x a una potencia n, sin utilizar el operador de exponente.
```python
>>>elevarNumero(5, 3)  	
125
```
## ordenarDigitos
Construir una función que reciba un número y ordenados de manera ascendente.
```python
>>>ordenarDigitos(435)  		
345
```

## disminuirMatriz
Dado una matriz de tamaño mxn aplanar en una lista aquellos elementos que sean impares, posteriormente transformarlo nuevamente una matriz cuadrada. Pueda ser que en el proceso de transforma a una matriz cuadrada sobren elementos.

### Ejmplo
```python
>>> matriz = [[5,88,0], [3,69,12], [51,3,71], [4,45,29]]
>>>disminuirMatriz(matriz)
# al aplanar en una lista [5,3,69,51,3,71,45,29]
[[5,3],[69,51]]
>>> matriz = [[5,89,0], [3,69,12], [51,3,71], [141,45,29]]
# al aplanar en una lista [5,89,3,69,51,3,71,141,45,29]
[[5,89,3],[69,51,3], [71,141,45]]
```
