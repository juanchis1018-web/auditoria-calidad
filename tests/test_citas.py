import pytest

from src.citas import calcular_copago


# Ejemplo de prueba (ya escrita para que vea el formato).
def test_particular_paga_todo():
    assert calcular_copago(100000, "particular") == 100000


# Prueba 1 (TDD): el afiliado contributivo paga el 10 %, redondeado a 2 decimales.
def test_contributivo_paga_diez_por_ciento():
    assert calcular_copago(50000, "contributivo") == 5000
    assert calcular_copago(33333.33, "contributivo") == 3333.33


# Prueba 2 (TDD): el afiliado subsidiado no paga copago.
def test_subsidiado_no_paga():
    assert calcular_copago(80000, "subsidiado") == 0


# Prueba 3 (TDD): valores inválidos lanzan ValueError.
@pytest.mark.parametrize(
    "valor, tipo",
    [
        (-1000, "contributivo"),  # valor negativo
        (50000, "prepagada"),     # tipo de afiliado inexistente
        (50000, ""),              # tipo vacío
    ],
)
def test_valores_invalidos_lanzan_error(valor, tipo):
    with pytest.raises(ValueError):
        calcular_copago(valor, tipo)
