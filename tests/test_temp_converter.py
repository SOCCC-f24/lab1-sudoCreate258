import pytest
from temp_converter import c2f

def test_c2f_pass():
    # Valid case for c2f, should pass with both correct and incorrect formula
    assert round(c2f(0), 2) == 32.0  # Freezing point of water

def test_c2f_fail_with_broken_formula():
    # This test should fail with the broken formula but pass with the correct one
    assert round(c2f(-40), 2) == -40.0  # -40°C should equal -40°F

def test_c2f_correct():
    # Check for correct formula behavior with other cases
    assert round(c2f(100), 2) == 212.0  # Boiling point of water
    assert round(c2f(37.78), 2) == 100.0  # Normal human body temperature
