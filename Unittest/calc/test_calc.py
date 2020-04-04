import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5,5),10)
        self.assertEqual(calc.add(-1,1),0)

    def test_subtrct(self):
        self.assertEqual(calc.subtract(6,3),3)
        self.assertEqual(calc.subtract(-1,1),-2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3,3),9)
        self.assertEqual(calc.multiply(-2,-3),6)

    def test_devide(self):
        self.assertEqual(calc.devide(6,2),3)
        self.assertEqual(calc.devide(-1,-1),1)
  
if __name__=='__main__':
 unittest.main()
