import pytest
from process import process


# Etapa 1: Cobertura de sentencias (Statement Coverage)
# Un solo valor positivo y par ejecuta todas las sentencias de la funcion.
@pytest.mark.statement
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2], ["positivo", "par"]),
    ],
    ids=["Prueba1_positivo_y_par"],
)
def test_statement_coverage(values, expected):
    assert process(values) == expected
