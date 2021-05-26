import hayDuplicadosEnLista;
import pytest;

Lista1 = [4, 8, 12]
Lista2 = [40, 8, 12]
Lista3 = []
Lista4 = [40, "8", 12]
Lista5 = [40, 8.5, 12]


def test_DuplicadoLista_1():
    assert hayDuplicadosEnLista.hayDuplicadosEnLista(Lista1) == True   
