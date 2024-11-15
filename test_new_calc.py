#тест,написанный смежником для проверки добавленных им в калькулятор функций sqrt_pow
import unittest
import calc


class NewCalcTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(calc.pow(3, 3), 27)
