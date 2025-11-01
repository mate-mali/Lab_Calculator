import calculator

def test_Add():
    calc = calculator.Calculator(2,1)
    assert calc.sum() == 3

def test_Subtract():
    calc = calculator.Calculator(2,5)
    assert calc.subtract() == -3

def test_Multiply():
    calc = calculator.Calculator(2,5)
    assert calc.multiply() == 10

def test_Divide1():
    calc = calculator.Calculator(2,5)
    assert calc.divide() == 0.4

def test_Divide2():
    calc = calculator.Calculator(2,0)
    # assert calc.divide() == 0
    assert calc.divide() == None #should raise error ane return None

def test_type3():
    calc = calculator.Calculator("tomasz",0)
    assert ValueError


