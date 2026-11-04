class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if (a < 0) and (b < 0):
            a = -a
            b = -b
            for i in range(b):
                result = self.add(result, a)
            return result
        
        elif (a < 0) and (b >= 0):
            a = -a
            b = b
            for i in range(b):
                result = self.add(result, a)
            return -result
        
        elif (a >= 0) and (b < 0):
            a = a
            b = -b
            for i in range(b):
                result = self.add(result, a)
            return -result
        else:
            a = a
            b = b
            for i in range(b):
                result = self.add(result, a)
            return result
        


    def divide(self, a, b):
        n1 = a if a >= 0 else -a
        n2 = b if b >= 0 else -b
        result = 0
        while n1 >= n2:
            n1 = self.subtract(n1, n2)
            result += 1

        if a < 0 or b < 0:
            return -result
        else:
            return result
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))