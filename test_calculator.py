# test_calculator.py
import pytest
from calculator import add, sub, mul, div

# Существующие тесты
def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(2, 4) == 8

def test_div():
    assert div(8, 2) == 4

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

# ===== НОВЫЕ ТЕСТЫ =====

# Негативные тесты
def test_add_negative():
    """Негативный тест: сложение отрицательных чисел"""
    assert add(-2, -3) == -5
    assert add(-5, 3) == -2

def test_sub_negative():
    """Негативный тест: вычитание с отрицательными"""
    assert sub(-5, -3) == -2
    assert sub(5, -3) == 8

# Граничные тесты
def test_add_large_numbers():
    """Граничный тест: очень большие числа"""
    assert add(10**9, 10**9) == 2 * 10**9

def test_mul_by_zero():
    """Граничный тест: умножение на ноль"""
    assert mul(100, 0) == 0
    assert mul(0, 100) == 0

def test_div_small_numbers():
    """Граничный тест: деление очень маленьких чисел"""
    assert div(1e-10, 1e-10) == 1.0