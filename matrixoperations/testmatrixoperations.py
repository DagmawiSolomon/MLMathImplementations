import unittest
from matrixoperations import MatrixOperations
class MatrixOperationsTestCase(unittest.TestCase):
    def setUp(self):
        self.mp = MatrixOperations
        
    def test_init_with_mixed_elements(self):
        with self.assertRaises(ValueError):
            self.mp(["a", 1, 2])
    def test_init_with_non_list_input(self):
        with self.assertRaises(TypeError):
            self.mp(1)
    def test_init_with_numeric_elements(self):
        self.mp([0,1])
        self.mp([-1,2])
        large_value = 458**58
        self.mp([1,large_value])
        
    def test_init_with_float_elements(self):
        self.mp([0.5,1.6])
        self.mp([-0.1,2.4])
        small_value = 2/(458**58)
        self.mp([1,small_value])
    def test_init_with_empty_list(self):
        self.mp([])
    
    def test_multidimensional_list(self):
        self.mp([[1,2],[3,4]])
        self.mp([[5,6],[7,8]])
        self.mp([[5,7,8],[4,5,8],[6,2,1]])
        
    def test_get_shape(self):
        x_1 = self.mp([[1,2,3],[4,5,6]])
        self.assertEqual(x_1.shape,(2,3))
        
        x_2 = self.mp([1,2,4])
        self.assertEqual(x_2.shape,(3,1))
        
        x_3 = self.mp([])
        self.assertEqual(x_3.shape,(0,0))
        
        with self.assertRaises(ValueError):
            self.mp([[1,2],[3,4],[5,6,7]])
            
        
    def test_addition(self):
        x = self.mp([[1, 2], [0, 0]])
        y = self.mp([[1, 2], [0, 0]])
        self.assertEqual(x + y, [[2, 4], [0, 0]])

        x = self.mp([[1, 2], [0, 0]])
        y = self.mp([[0, 0], [0, 0]])
        result = [[1, 2], [0, 0]]
        self.assertEqual(x + y, result)

        x = self.mp([[1, 2], [0, 0]])
        y = self.mp([[-1, -2], [0, 0]])
        result = [[0, 0], [0, 0]]
        self.assertEqual(x + y, result)

        x = self.mp([[1, 2], [0, 0]])
        y = self.mp([[1.5, 2.5], [0.5, 0.5]])
        result = [[2.5, 4.5], [0.5, 0.5]]
        self.assertEqual(x + y, result)
          
        x = self.mp([1,2])
        y = self.mp([2,3])
        self.assertEqual(x+y,[3,5])
        
    def test_subtraction(self):
        x = self.mp([[1, 2], [0, 0]])
        y = self.mp([[1, 2], [0, 0]])
        self.assertEqual(x - y, [[0, 0], [0, 0]])

        x = self.mp([[1, 2], [0, 0]])
        y = self.mp([[0, 0], [0, 0]])
        result = [[1, 2], [0, 0]]
        self.assertEqual(x - y, result)

        x = self.mp([[1, 2], [0, 0]])
        y = self.mp([[-1, -2], [0, 0]])
        result = [[2, 4], [0, 0]]
        self.assertEqual(x - y, result)

        x = self.mp([[1, 2], [0, 0]])
        y = self.mp([[1.5, 2.5], [0.5, 0.5]])
        result = [[-0.5, -0.5], [-0.5, -0.5]]
        self.assertEqual(x - y, result)
          
        x = self.mp([1,2])
        y = self.mp([2,3])
        self.assertEqual(x-y,[-1,-1])

    
            
if __name__ == '__main__':
    unittest.main()