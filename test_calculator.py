import pytest
import calculator
import coverage

def test_Add():
    calc = calculator.Calculator(2,1)
    assert calc.sum() == 3
    # assert calc.sum() == 5

def test_Subtract():
    calc = calculator.Calculator(2,5)
    assert calc.subtract() == -3
    # assert calc.subtract() == 0

def test_Multiply():
    calc = calculator.Calculator(2,5)
    assert calc.multiply() == 10
    # assert calc.subtract() == 2

def test_Divide1():
    calc = calculator.Calculator(2,5)
    assert calc.divide() == 0.4

def test_Divide2():
    calc = calculator.Calculator(2,0)
    # assert calc.divide() == 0
    assert calc.divide() == None #should raise error ane return None

def test_Types_Conversions():
    calc = calculator.Calculator("3", '3')
    assert calc.sum() == 6
    assert calc.subtract() == 0
    assert calc.multiply() == 9.0
    assert calc.divide() == 1


def test_Types_Conversions_text():
    calc = calculator.Calculator("3", 'Mateusz')
    assert calc.sum() == 6
    assert calc.subtract() == 0
    assert calc.multiply() == 9.0
    assert calc.divide() == 1

def test_Types_Conversions_text2():
    calc = calculator.Calculator("tomasz", '2.75')
    assert calc.sum() == 6
    assert calc.subtract() == 0
    assert calc.multiply() == 9.0
    assert calc.divide() == 1