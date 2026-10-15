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


# Etapa 3: Cobertura de caminos (Path Coverage) con 2 valores
# Cada valor sigue 1 de 4 rutas -> 4 x 4 = 16 caminos.
@pytest.mark.path
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2, 4], ["positivo", "par", "positivo", "par"]),
        ([2, 3], ["positivo", "par", "positivo"]),
        ([2, -2], ["positivo", "par", "par"]),
        ([2, -3], ["positivo", "par"]),
        ([3, 2], ["positivo", "positivo", "par"]),
        ([3, 5], ["positivo", "positivo"]),
        ([3, -2], ["positivo", "par"]),
        ([3, -3], ["positivo"]),
        ([-2, 2], ["par", "positivo", "par"]),
        ([-2, 3], ["par", "positivo"]),
        ([-2, -4], ["par", "par"]),
        ([-2, -3], ["par"]),
        ([-3, 2], ["positivo", "par"]),
        ([-3, 3], ["positivo"]),
        ([-3, -2], ["par"]),
        ([-3, -5], []),
    ],
    ids=[f"Prueba{i}" for i in range(1, 17)],
)
def test_path_coverage(values, expected):
    assert process(values) == expected
