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
    
    
            
if __name__ == '__main__':
    unittest.main()