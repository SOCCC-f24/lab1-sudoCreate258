import pytest
from temp_converter import f2c  # Assuming f2c is your Fahrenheit to Celsius function

def test_f2c_correct():
    # Valid case, 212°F should be 100°C
    assert f2c(212) == 100.0

def test_f2c_fail_case_1():
    # Test with a small decimal, 32.18°F should be approximately 0.1°C
    assert f2c(32.18) == 0.1

def test_f2c_fail_case_2():
    # Test with a negative value, -40°F should be -40°C
    assert f2c(-40) == -40.0

def test_f2c_fail_case_3():
    # Test with extreme value, -459.67°F should be -273.15°C
    assert f2c(-459.67) == -273.15
