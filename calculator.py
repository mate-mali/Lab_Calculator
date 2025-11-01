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
           print("Second value is of non-numeric nature")
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
        try:
            return self.op1 / self.op2
        except ZeroDivisionError:
            print("Divisor should not be 0!")
