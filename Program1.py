class Calculator:
    def __init__(self,a,b,operation):
        self.a=a
        self.b=b
        self.operation=operation.lower()
    def calculate(self):
        if self.operation=="add":
            return self.a+self.b
        elif self.operation=="subtract":
            return self.a-self.b
        elif self.operation=="multiply":
            return self.a*self.b
        elif self.operation=="divide":
            if self.b==0:
                return "Error:The Value cannot divisible by zero."
            return self.a/self.b
        elif self.operation=="modular division":
            if self.a==0 or self.b==0:
                return "Error:The value zero cannot be divisible"
            return self.a%self.b
        else:
            return "Error: Invalid operation."
cal=Calculator(10.0,5.0,"divide")
result=cal.calculate()
print(f'Result: {result}')
