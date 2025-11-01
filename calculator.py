class Calculator:
    def __init__(self, op1: float, op2: float):
       try:
           op1 = float(op1)
       except ValueError:
           print("First value is of non-numeric nature")
           raise TypeError("Unsupported Value Type, Please change parameters")

       try:
           op2 = float(op2)
       except ValueError:
           print("First value is of non-numeric nature")
           raise TypeError("Unsupported Value Type, Please change parameters")

       self.op1 = op1
       self.op2 = op2

    def sum(self):
        return self.op1+self.op2

    def subtract(self):
        return self.op1-self.op2

    def multiply(self):
        return self.op1 * self.op2

    def divide(self):
        #assert self.op2 != 0, "Divisor should not be 0"
        # if self.op2 == 0:
        #     raise ZeroDivisionError("Divisor should not be 0!")
        try:
            return self.op1 / self.op2
        except ZeroDivisionError:
            print("Divisor should not be 0!")



calc = Calculator(2,4)

print(f"Run for 2 and 4")
print("Sum: ", calc.sum())
print("Subtract: ", calc.subtract())
print("Multiply: ", calc.multiply())
print("Divide: ", calc.divide())

calc2 = Calculator(4,0)

print(f"Run for 4 and 0")
print("Sum: ", calc2.sum())
print("Subtract: ", calc2.subtract())
print("Multiply: ", calc2.multiply())
print("Divide: ", calc2.divide())

calc3 = Calculator("5",2)
print(f"Run for '5'' and 0")
print("Sum: ", calc3.sum())
print("Subtract: ", calc3.subtract())
print("Multiply: ", calc3.multiply())
print("Divide: ", calc3.divide())

calc4 = Calculator("1","Mateusz")
print(f"Run for '5'' and 'Mateusz'")
print("Sum: ", calc4.sum())
print("Subtract: ", calc4.subtract())
print("Multiply: ", calc4.multiply())
print("Divide: ", calc4.divide())