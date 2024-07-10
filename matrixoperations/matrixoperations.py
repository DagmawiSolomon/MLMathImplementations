from itertools import chain

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix
        self.validate_matrix()
       
                
    def flatten(self):
        if len(self.matrix) > 0 and isinstance(self.matrix[0], list):
            return list(chain.from_iterable(self.matrix))
        else:
            return self.matrix

    def validate_matrix(self):
        
        if not isinstance(self.flatten(), list):
            raise TypeError("Input must be a list")
        for element in self.flatten():
            if not isinstance(element, (int,float)):
                raise ValueError("All elements in the list be a number type(int or float)")
            
    
    def __add__(self, other):
        pass

    def __sub__(self,other):
        pass

    def __mul__(self,other):
        pass

    def __floordiv__(self,other):
        pass

    def determinent(self):
        pass



