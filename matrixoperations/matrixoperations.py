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
        
        """
        Adds another matrix or vector to this matrix or vector.

        Args:
            other (Matrix or list): The matrix or vector to add.

        Raises:
            ValueError: If the matrices or vectors do not have the same dimensions.
            TypeError: If the other operand is not a Matrix instance or a list (vector).

        Returns:
            Matrix or list: A new Matrix instance or list representing the sum.
        """
        if isinstance(other, type(self)):
            if self.shape == other.shape:
                result = []
                row, col = self.shape
                if (col != 1):
                    for i in range(row):
                        row_result = []
                        for j in range(col):
                            row_result.append(self.matrix[i][j] + other.matrix[i][j])
                        result.append(row_result)
                else:
                    for i in range(row):
                        result.append(self.matrix[i] + other.matrix[i])
                return result
            else:
                raise ValueError("Matrices must have the same dimensions to add")
        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self).__name__, type(other).__name__))

            
        

    def __sub__(self,other):
        """
        Subtracts another matrix or vector from this matrix or vector.

        Args:
            other (Matrix or list): The matrix or vector to subtract.

        Raises:
            ValueError: If the matrices or vectors do not have the same dimensions.
            TypeError: If the other operand is not a Matrix instance or a list (vector).

        Returns:
            Matrix or list: A new Matrix instance or list representing the difference.
        """
        if isinstance(other, type(self)):
            if self.shape == other.shape:
                result = []
                row, col = self.shape
                if (col != 1):
                    for i in range(row):
                        row_result = []
                        for j in range(col):
                            row_result.append(self.matrix[i][j] - other.matrix[i][j])
                        result.append(row_result)
                else:
                    for i in range(row):
                        result.append(self.matrix[i] - other.matrix[i])
                return result
            else:
                raise ValueError("Matrices must have the same dimensions to add")
        else:
            raise TypeError("Unsupported operand type(s) for -: '{}' and '{}'".format(type(self).__name__, type(other).__name__))   

    def __mul__(self,other):
        """
        Multiplies another matrix or vector with this matrix or vector.

        Args:
            other (Matrix or list): The matrix or vector to multiply.

        Raises:
            ValueError: If the matrices or vectors do not have the same dimensions.
            TypeError: If the other operand is not a Matrix instance or a list (vector).

        Returns:
            Matrix or list: A new Matrix instance or list representing the product.
        """
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
    
    



