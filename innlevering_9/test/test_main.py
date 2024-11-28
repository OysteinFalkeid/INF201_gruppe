import pytest
from Exercise_9 import Complex

def test_re():
    complex = Complex(1)
    assert complex.re == 1, f'value must be 1'
    