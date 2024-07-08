import unittest
from matrixoperations import MatrixOperations
class MatrixOperationsTestCase(unittest.TestCase):
    def setUp(self):
        self.mp = MatrixOperations()
        
    def test_matrix(self):
        self.mp.matrix([0,1,2])
        self.mp.matrix([[0,1,2],[3,4,5]])
        with self.assertRaises(TypeError):
            self.mp.matrix(0)
        with self.assertRaises(ValueError):
            self.mp.matrix([0,1,2,"3"])
            
            
if __name__ == '__main__':
    unittest.main()