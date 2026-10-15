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


# Etapa 2: Cobertura de ramas (Branch Coverage)
# Cada decision (for, value > 0, value % 2 == 0) toma su rama Si y su rama No.
@pytest.mark.branch
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2, -1], ["positivo", "par"]),
        ([], []),
    ],
    ids=["Prueba1_ramas_si_y_no", "Prueba2_lista_vacia"],
)
def test_branch_coverage(values, expected):
    assert process(values) == expected
