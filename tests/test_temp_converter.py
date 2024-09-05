import pytest
from temp_converter import c2f

def test_c2f_pass():
    # Valid case, 0°C should be 32°F
    assert c2f(0) == 32.0

def test_c2f_fail_case_1():
    # Test with small decimal, 0.1°C should be 32.18°F
    assert c2f(0.1) == 32.18

def test_c2f_fail_case_2():
    # Test with a negative value, -17.78°C should be 0°F
    assert c2f(-17.78) == 0.0

def test_c2f_fail_case_3():
    # Test with large decimal, 100.1°C should be 212.18°F
    assert c2f(100.1) == 212.18

def test_c2f_fail_case_4():
    # Test with extreme value, -273.15°C should be -459.67°F
    assert c2f(-273.15) == -459.67
