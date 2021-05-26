import portafolio3;
import pytest;

Lista1 = [4, 8, 12]
Lista2 = [40, 8, 12]
Lista3 = []
Lista4 = [40, "8", 12]
Lista5 = [40, 8.5, 12]


def test_construir_1():
    assert portafolio3.construir(2345) == 24   

def test_construir_2():
    assert portafolio3.construir(2345) == 'No hay digitos pares'     
    
def test_construir_3():
    assert portafolio3.construir('ABC') == 'Error: Tipo de dato incorrecto'
    
def test_construir_4():
    assert portafolio3.construir(125.8) == 'Error: Tipo de dato incorrecto'    
    
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
    assert portafolio3.elevarNumero(0, -2)  == 0
    
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
    
    

    
