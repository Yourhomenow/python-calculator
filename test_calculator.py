import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(7, 2), 9)
        self.assertEqual(self.calc.add(-5, 2), -3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,4), 1)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,4), 20)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(5,5), 1)
        self.assertEqual(self.calc.divide(-10,5), -2)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9,2), 1)
        self.assertEqual(self.calc.modulo(2,1), 0)    
if __name__ == '__main__':
    unittest.main()