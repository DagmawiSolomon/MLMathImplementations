class MatrixOperations:
    def __init__(self):
        pass
        
    def matrix(self,arr):
        if not isinstance(arr, list):
            raise TypeError("Input must be a list")
        for element in arr:
            if not isinstance(element, (int,float)):
                raise ValueError("All elements in the list be a number type(int or float)")
    
    def multiply(self):
        pass

    def addition(self):
        pass

    def subtraction(self):
        pass

    def division(self):
        pass

    def determinent(self):
        pass




# import matrixoperations as matrix
# x = mp.matrix([0,1,2])
# y = mp.matrix([0,1,2])
# x + y, x-y, x*y, x/y

