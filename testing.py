import portafolio3;
import pytest;

def test_construir_1():
    assert portafolio3.construir(2345) == 24   

def test_construir_2():
    assert portafolio3.construir(1135) == 'No hay digitos pares'     
    
def test_construir_3():
    assert portafolio3.construir('ABC') == 'Error: Tipo de dato incorrecto'
    
def test_construir_4():
    assert portafolio3.construir(125.8) == 'Error: Tipo de dato incorrecto'    

def test_construir_5():
    assert portafolio3.construir(200336) == 2006     
    
#digitoMenor    

def test_digitoMenor_1():
    assert portafolio3.digitoMenor(569803)  == 0
    
def test_digitoMenor_2():
    assert portafolio3.digitoMenor(777)  == 7
    
def test_digitoMenor_3():
    assert portafolio3.digitoMenor(8563266)  == 2
    
def test_digitoMenor_4():
    assert portafolio3.digitoMenor(5)  == 5
    
#digitosOrdenados  

def test_digitosOrdenados_1():
    assert portafolio3.digitosOrdenados(2345678)  == True
    
def test_digitosOrdenados_2():
    assert portafolio3.digitosOrdenados(2345618)  == False
    
def test_digitosOrdenados_3():
    assert portafolio3.digitosOrdenados(2)  == True    
    
def test_digitosOrdenados_4():
    assert portafolio3.digitosOrdenados(28)  == True    
    
def test_digitosOrdenados_1():
    assert portafolio3.digitosOrdenados(23.5)  == 'Error: Tipo de dato incorrecto' 
    
#elevarNumero

def test_elevarNumero_1():
    assert portafolio3.elevarNumero(5, 3)  == 125
    
def test_elevarNumero_2():
    assert portafolio3.elevarNumero(5, -1)  == "El exponente debe ser positivo y entero"

def test_elevarNumero_3():
    assert portafolio3.elevarNumero(5, 5.2)  == "El exponente debe ser positivo y entero"
    
def test_elevarNumero_4():
    assert portafolio3.elevarNumero(0, 2)  == 0
    
#ordenarDigitos

def test_ordenarDigitos_1():
    assert portafolio3.ordenarDigitos(354)  == 345
    
def test_ordenarDigitos_2():
    assert portafolio3.ordenarDigitos(354.5)  == "Error: El parámetro debe ser positivo y entero"
    
def test_ordenarDigitos_3():
    assert portafolio3.ordenarDigitos(-354)  == "Error: El parámetro debe ser positivo y entero"    
    
def test_ordenarDigitos_4():
    assert portafolio3.ordenarDigitos(222)  == 222

def test_ordenarDigitos_5():
    assert portafolio3.ordenarDigitos(15009)  == 159
    
#disminuirMatriz

m = [[5,88,0], [3,69,12], [51,3,71], [4,45,29]]
n = [[5,89,0], [3,69,12], [51,3,71], [141,45,29]]
l = [[5,89,0, 0], [141,45,29]]

def test_disminuirMatriz_1():
    assert portafolio3.disminuirMatriz(m)  == [[5,3],[69,51]]

def test_disminuirMatriz_2():
    assert portafolio3.disminuirMatriz(n)  == [[5,89,3],[69,51,3], [71,141,45]]
    
def test_disminuirMatriz_3():
    assert portafolio3.disminuirMatriz(l)  == 'Error: existen vectores de diferentes tamaños'
    
