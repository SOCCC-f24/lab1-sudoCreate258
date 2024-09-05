import pytest
from temp_converter import c2f

def test_c2f_pass():
    # Correct conversion for 0°C to 32°F
    assert c2f(0) == 32.0

def test_c2f_fail_case_1():
    # Test case with a small decimal that may fail without parentheses
    assert c2f(0.1) == 32.18

def test_c2f_fail_case_2():
    # Test case with a negative value where parentheses may affect the result
    assert c2f(-17.78) == 0.0  # -17.78°C should equal 0°F

def test_c2f_fail_case_3():
    # Edge case with large decimal
    assert c2f(100.1) == 212.18

def test_c2f_fail_case_4():
    # Testing large negative value
    assert c2f(-273.15) == -459.67  # Absolute zero in Fahrenheit
