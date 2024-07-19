from itertools import chain

class MatrixOperations:
    """
    A class to perform various operations on matrices and vectors.

    Attributes:
        matrix (list): The matrix represented as a list of lists or vector as a list.
        shape (tuple): The shape of the matrix as a tuple (num_rows, num_cols).
    """

    def __init__(self, matrix):
        """
        Initializes the MatrixOperations object with the given matrix.

        Args:
            matrix (list): The matrix to be operated upon.
        """
        self.matrix = matrix
        self.validate_matrix()
        self.shape = self.get_shape()

    def flatten(self):
        """
        Flattens the matrix into a 1-dimensional list.

        Returns:
            list: Flattened list representation of the matrix.
        """
        if len(self.matrix) > 0 and isinstance(self.matrix[0], list):
            return list(chain.from_iterable(self.matrix))
        else:
            return self.matrix

    def get_shape(self):
        """
        Determines the shape of the matrix.

        Returns:
            tuple: A tuple representing the shape of the matrix (num_rows, num_cols).
        """
        if not self.matrix:
            return (0, 0)

        if isinstance(self.matrix[0], list):
            num_rows = len(self.matrix)
            num_cols = len(self.matrix[0])

            for row in self.matrix:
                if len(row) != num_cols:
                    raise ValueError("All rows must have the same number of columns")

            return (num_rows, num_cols)
        else:
            return (len(self.matrix), 1)

    def validate_matrix(self):
        """
        Validates the matrix to ensure it is a valid list of numbers.

        Raises:
            TypeError: If the matrix is not a list.
            ValueError: If any element in the matrix is not a number (int or float).
        """
        if not isinstance(self.flatten(), list):
            raise TypeError("Input must be a list")
        for element in self.flatten():
            if not isinstance(element, (int, float)):
                raise ValueError("All elements in the list must be of type int or float")

    def __add__(self, other):
        """
        Adds another matrix or vector to this matrix or vector.

        Args:
            other (Matrix or list): The matrix or vector to add.

        Raises:
            ValueError: If the matrices or vectors do not have the same dimensions.
            TypeError: If the other operand is not a Matrix instance or a list (vector).

        Returns:
            list: A new list representing the sum of matrices or vectors.
        """
        if isinstance(other, type(self)):
            if self.shape == other.shape:
                result = []
                row, col = self.shape
                if col != 1:
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

    def __sub__(self, other):
        """
        Subtracts another matrix or vector from this matrix or vector.

        Args:
            other (Matrix or list): The matrix or vector to subtract.

        Raises:
            ValueError: If the matrices or vectors do not have the same dimensions.
            TypeError: If the other operand is not a Matrix instance or a list (vector).

        Returns:
            list: A new list representing the difference of matrices or vectors.
        """
        if isinstance(other, type(self)):
            if self.shape == other.shape:
                result = []
                row, col = self.shape
                if col != 1:
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
                raise ValueError("Matrices must have the same dimensions to subtract")
        else:
            raise TypeError("Unsupported operand type(s) for -: '{}' and '{}'".format(type(self).__name__, type(other).__name__))

    def __mul__(self, other):
        """
        Multiplies another matrix or vector with this matrix or vector.

        Args:
            other (Matrix or list): The matrix or vector to multiply.

        Raises:
            ValueError: If the matrices or vectors do not have the compatible dimensions.
            TypeError: If the other operand is not a Matrix instance or a list (vector).

        Returns:
            list: A new list representing the product of matrices or vectors.
        """
      
        n = len(self.matrix)         
        m = len(self.matrix[0])    
        p = len(other.matrix[0])   

        result = [[0] * p for _ in range(n)]

        for i in range(n):
            for j in range(p):
                for k in range(m):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return result

    def __truediv__(self, other):
        """
        Divides this matrix by another matrix or scalar.

        Args:
            other (int, float, Matrix): The scalar or matrix to divide by.

        Returns:
            list: A new list representing the result of division.
        """
        pass

    def inverse(self):
        """
        Calculates the inverse of the matrix.

        Returns:
            list: A new list representing the inverse of the matrix.
        """
        pass

    def determinant(self):
        """
        Calculates the determinant of the matrix.

        Returns:
            float: The determinant value of the matrix.
        """
        pass

    def eigenvalues(self):
        """
        Calculates the eigenvalues of the matrix.

        Returns:
            list: A list of eigenvalues of the matrix.
        """
        pass

    def eigenvectors(self):
        """
        Calculates the eigenvectors of the matrix.

        Returns:
            list: A list of eigenvectors of the matrix.
        """
        pass
