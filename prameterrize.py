import pytest

import lennardjones as lj


@pytest.mark.parametrize(
    "distance, sigma, epsilon, expected",
    [
        (1.8, 2, 0.01, 0.0663611895325),
        (2, 2, 0.01, 0),
        (2.5, 2, 0.01, -0.00773698093056),
        (4.5, 2, 0.01, -0.00030591773748),
    ],
)
def test_lennard_jones_energy(distance, sigma, epsilon, expected):
    result = lj.energy(distance, sigma, epsilon)
    assert result == pytest.approx(
        expected, abs=1e-8
    ), f"Actual: {result} != Expected: {expected}"
