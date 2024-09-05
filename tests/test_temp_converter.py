import pytest
from temp_converter import c2f

def test_c2f_pass():
    # Valid case for c2f
    assert round(c2f(0), 2) == 32.0  # Freezing point of water

def test_c2f_pass_case_2():
    # Valid case for c2f
    assert round(c2f(100), 2) == 212.0  # Boiling point of water

def test_c2f_pass_case_3():
    # Valid case for c2f
    assert round(c2f(37.78), 2) == 100.0  # Normal human body temperature
