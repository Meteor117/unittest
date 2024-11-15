# систематизируем тестирование test_calc2.py

import unittest
import test_calc2
import test_new_calc

calcST = unittest.TestSuite()
# calcST.addTest(unittest.makeSuite(test_calc.CalcTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calc2.CalcTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.NewCalcTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.NewCalcTest))

runner = unittest.TextTestRunner()#verbosity=2
runner.run(calcST)

