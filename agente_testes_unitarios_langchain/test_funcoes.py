
import pytest
from funcoes import somar, dividir

def test_somar_positivos():
    assert somar(2, 3) == 5

def test_somar_negativos():
    assert somar(-2, -3) == -5

def test_somar_positivo_negativo():
    assert somar(2, -3) == -1

def test_somar_zero():
    assert somar(0, 0) == 0

def test_somar_float():
    assert somar(2.5, 3.5) == 6.0

def test_dividir_positivos():
    assert dividir(10, 2) == 5.0

def test_dividir_negativos():
    assert dividir(-10, -2) == 5.0

def test_dividir_positivo_negativo():
    assert dividir(10, -2) == -5.0

def test_dividir_negativo_positivo():
    assert dividir(-10, 2) == -5.0

def test_dividir_por_zero():
    with pytest.raises(ValueError) as e:
        dividir(10, 0)
    assert str(e.value) == "Divisor não pode ser zero."

def test_dividir_float():
    assert dividir(10.0, 2.0) == 5.0

def test_dividir_zero_por_numero():
    assert dividir(0, 5) == 0.0
