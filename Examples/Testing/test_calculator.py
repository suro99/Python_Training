import unittest
import sys
import calculator   # import the file
 
class TestCalculator(unittest.TestCase):
   
    def test_add(self):
        self.assertEqual(calculator.add(2,3),5)
        self.assertEqual(calculator.add(-2,-3),-1)
       
    @unittest.skip(" we will skip this test method for time being")    
    def test_subtract(self):
        self.assertEqual(calculator.subtract(10,5),2)
       
    @unittest.skipIf(sys.platform == "Ubuntu", "this will not run on windows")    
    def test_multiply(self):
        self.assertEqual(calculator.multiply(10,5),50)  
       
    def test_divide(self):
        self.assertEqual(calculator.divide(10,5),2)
        with self.assertRaises(ValueError):
            calculator.divide(10,0)
           
if __name__ == "__main__":
    unittest.main()