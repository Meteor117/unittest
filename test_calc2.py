#test calc.py with unittest

import calc
import unittest
import random

class CalcTest(unittest.TestCase):
    #@unittest.skip("Не нравится")#тупо пропускаем тест с указанием причины
    def test_add(self):
        self.assertEqual(calc.add(1, 2),3)
    #@unittest.skipIf(random.randint(0, 2), "Не повезло")#пропускает тест рандомно - 0/1(True/False)
    def test_sub(self):                                         #True - пропускаем,False - не пропускаем
        self.assertEqual(calc.sub(5, 3),2)
    def test_mul(self):
        self.assertEqual(calc.mul(2, 3), 6)
    def test_div(self):
        self.assertEqual(calc.div(6, 3), 2)

if __name__ == '__main__':
    unittest.main()





