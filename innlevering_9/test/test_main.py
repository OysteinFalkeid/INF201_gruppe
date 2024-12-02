import pytest
from Exercise_9 import Complex

def test_re():
    complex = Complex(1)
    assert complex.re == 1, f'Complex.re should be 1 but in {complex.re}'

def test_im():
    complex = Complex(None, 1)
    assert complex.im == 1, f'Complex.im should be 1 but is {complex.im}'

def test_add_with_real():
    complex = Complex(1, 2)
    result = complex + 1
    assert result.re == 2 and result.im == 2, f'Complex should be 2 + 2i but is {result}'

def test_add_with_complex():
    complex = Complex(1, 2)
    result = complex + Complex(1, 1)
    assert result.re == 2 and result.im == 3, f'Complex should be 2 + 3i but is {result}'

def test_radd_with_real():
    complex = Complex(1, 2)
    result = 1 + complex
    assert result.re == 2 and result.im == 2, f'Complex should be 2 + 2i but is {result}'

def test_sub_with_real():
    complex = Complex(1, 2)
    result = complex - 1
    assert result.re == 0 and result.im == 2, f'Complex should be 2 + 2i but is {result}'

def test_sub_with_complex():
    complex = Complex(1, 2)
    result = complex - Complex(1, 1)
    assert result.re == 0 and result.im == 1, f'Complex should be 2 + 3i but is {result}'

def test_rsub_with_real():
    complex = Complex(1, 2)
    result = 1 - complex
    assert result.re == 0 and result.im == -2, f'Complex should be 2 + 2i but is {result}'

def test_mul_with_real():
    complex = Complex(2, 3)
    result = complex * 2
    assert result.re == 4 and result.im == 6, f'Complex should be 2 + 2i but is {result}'

def test_mul_with_complex():
    complex = Complex(2, 3)
    result = complex * Complex(2, 2)
    assert result.re == -2 and result.im == 10, f'Complex should be 2 + 3i but is {result}'

def test_rmul_with_real():
    complex = Complex(2, 3)
    result = 2 * complex
    assert result.re == 4 and result.im == 6, f'Complex should be 2 + 2i but is {result}'

def test_div_with_real():
    complex = Complex(2, 4)
    result = complex / 2
    assert result.re == 1 and result.im == 2, f'Complex should be 2 + 2i but is {result}'

def test_div_with_complex():
    complex = Complex(2, 4)
    result = complex / Complex(2, 2)
    assert result.re == (3/2) and result.im == (1/2), f'Complex should be 2 + 3i but is {result}'

def test_rdiv_with_real():
    complex = Complex(2, 4)
    result = 2 / complex
    assert result.re == 0.2 and result.im == -0.4, f'Complex should be 2 + 2i but is {result}'