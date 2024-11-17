import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 1+2)
        self.assertEqual(self.calc.add(3, -4), 3+(-4))
        self.assertEqual(self.calc.add(3, 0), 3+0)

    def test_substract(self):
        self.assertEqual(self.calc.subtract(2, 0), 2-0)
        self.assertEqual(self.calc.subtract(3, 10), 3-10)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, -3), 1*-3)    # b เป็นลบ
        self.assertEqual(self.calc.multiply(-3, -2), -3*-2)    # a และ b เป็นลบ
        self.assertEqual(self.calc.multiply(-1, 3), -1*3)    # a เป็นลบ
        self.assertEqual(self.calc.multiply(3, 5), 3*5)     # แบบปกติ
        self.assertEqual(self.calc.multiply(3, 0), 3*0)      # a คูณด้วย 0
        self.assertEqual(self.calc.multiply(0, 3), 0*3)      # b คูณด้วย 0
        self.assertEqual(self.calc.multiply(0, 0), 0*0)      # a และ b เป็น 0

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 1), 2)        # หารลงตัว
        self.assertEqual(self.calc.divide(30, 7), 4)       # หารไม่ลงตัว
        self.assertEqual(self.calc.divide(0, 2), 0)        # a เป็น 0
        self.assertEqual(self.calc.divide(2, 0), None)     # a หารด้วย 0
        self.assertEqual(self.calc.divide(0, 0), None)     # 0 หารด้วย 0
        self.assertEqual(self.calc.divide(7, 7), 1)        # ตัวเศษและส่วนเท่ากัน 
        self.assertEqual(self.calc.divide(-3, -3), 1)      # a และ b เป็นลบ
        self.assertEqual(self.calc.divide(-3, 4), 0)       # a เป็นลบ
        self.assertEqual(self.calc.divide(3, -4), 0)      # b เป็นลบ
        self.assertEqual(self.calc.divide(-4, 3), -1)       # a เป็นลบ
        self.assertEqual(self.calc.divide(4, -3), -1)      # b เป็นลบ

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 0), None)     # mod ด้วย 0
        self.assertEqual(self.calc.modulo(4, 10), 4%10)    # mod ด้วยจำนวนที่มากกว่า
        self.assertEqual(self.calc.modulo(4, 3), 4%3)      # mod แบบธรรมดา
        self.assertEqual(self.calc.modulo(4, 4), 4%4)      # a mod a
        self.assertEqual(self.calc.modulo(0, 0), None)     # 0 mod 0
        self.assertEqual(self.calc.modulo(-4, 3), -4%3)    # - mod +
        self.assertEqual(self.calc.modulo(4, -3), 4%-3)    # + mod -
        self.assertEqual(self.calc.modulo(-5, -3), -5%-3)  # - mod -
        self.assertEqual(self.calc.modulo(5, 3), 5%3)      # + mod +
        self.assertEqual(self.calc.modulo(-5, -6), -5%-6)  # - mod -
        self.assertEqual(self.calc.modulo(5, 6), 5%6)      # + mod +

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()