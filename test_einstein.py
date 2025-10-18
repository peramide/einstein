import pytest

from einstein import energy

def main():
    test_energy()


def test_energy():
    assert energy(1) == 90000000000000000
    assert energy(0) == 0
    assert energy(-1) == -90000000000000000