from itertools import chain

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix
        self.validate_matrix()
        self.shape = self.get_shape()
       
                
    def flatten(self):
        if len(self.matrix) > 0 and isinstance(self.matrix[0], list):
            return list(chain.from_iterable(self.matrix))
        else:
            return self.matrix
        
    def get_shape(self):
        if not self.matrix:
            return (0,0)
        
        if isinstance(self.matrix[0], list):
            num_rows = len(self.matrix)
            num_cols = len(self.matrix[0])
            
            for row in self.matrix:
                if len(row) != num_cols:
                    raise ValueError("All rows must have the same number of columns")
    
            return (num_rows, num_cols)
        else:
            return (len(self.matrix),1) 

    def validate_matrix(self):
        
        if not isinstance(self.flatten(), list):
            raise TypeError("Input must be a list")
        for element in self.flatten():
            if not isinstance(element, (int,float)):
                raise ValueError("All elements in the list be a number type(int or float)")
            
    
    def __add__(self, other):
        if self.shape == other.shape:
            sum = []
            row,col = self.shape
            for i in range(row):
                local_sum = []
                for j in range(col):
                    local_sum.append(self.matrix[i][j] + other.matrix[i][j])
                sum.append(local_sum)
            return sum
            
        

    def __sub__(self,other):
        pass

    def __mul__(self,other):
        pass

    def __floordiv__(self,other):
        pass

    def determinent(self):
        pass
    
    def inverse(self):
        pass
    
    def eigenvalues(self):
        pass
    
    def eigenvectors(self):
        pass
    
    



