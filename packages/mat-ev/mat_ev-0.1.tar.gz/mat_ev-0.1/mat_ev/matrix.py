import numpy as np

class Matrix:
    """ This class represents a fingerprint for a matrix object.
    It allows to compute the basic operations between matrices.
    
    Attributes:
        -det (float): determinant of the matrix
        -n_rows (integer): number of rows of the matrix
        -n_cols (integer): number of columns of the matrix
        -rows (list of lists): lists of rows of the matrix
    """
    
    
    #Constructor method
    def __init__(self,nested_lists):
        
        """ This function creates a matrix from nested lists
        
        Args: -nested_lists (list of lists): list containing lists of the rows of the matrix
        
        Returns: None
        """
        self.rows = nested_lists
        self.n_rows = len(nested_lists)
        self.n_cols = len(nested_lists[0])
        if self.n_rows == self.n_cols:
            self.det = self.calculate_det()
        else:
            self.det = np.NaN
        
        
    def calculate_det(self):
            
        """This method computes the determinant of the matrix
        
        Args: None 
        
        Returns: returns the determinant of the matrix (float)
        """  
        try:
            assert self.n_rows == self.n_cols, "The number of rows must be equal to the number of columns"
        except AssertionError as error:
            raise
        
        #Create the numpy matrix
        mat = np.array(self.rows)
        
        #Return the computed determinant 
        return round(np.linalg.det(mat),2)
    
    def calculate_inverse(self):
        """Method to compute the inverse of the matrix
        
        Args: None
        
        Returns: returns the inverse of the matrix
        """
        try:
            assert self.n_rows == self.n_cols, "This is not a square matrix"
        except AssertiontError as error:
            raise
        
        mat = np.array(self.rows)
        inverted =Matrix(list(np.linalg.inv(mat)))
        return inverted
    
    def __add__(self,other):
        
        """Magic method: ovverrides the usual behaviour of the "+" operator
        
        Args: -other(Matrix obj): the second matrix to be added
        
        Returns: the Matrix obj resulted from the addition of the 2 starting ones
        """
        try:
            assert (self.n_cols == other.n_cols) & (self.n_rows == other.n_rows), "The two matrices have different dimensions"
        except AssertionError as error:
            raise
        
        result = Matrix([[0],[0]])
        
        mat_1 = np.array(self.rows)
        mat_2 = np.array(other.rows)
        
        mat_3 = mat_1+mat_2
        
        result.rows = list(mat_3)
        result.n_cols = self.n_cols
        result.n_rows = self.n_rows
        result.det = result.calculate_det()
        
        return result
    

    def __sub__(self,other):
        
        """Magic method: ovverrides the usual behaviour of the "-" operator
        
        Args: -other(Matrix obj): the second matrix to be added
        
        Returns: the Matrix obj resulted from the subtraction of the 2 starting ones
        """
        
        try:
            assert (self.n_cols == other.n_cols) & (self.n_rows == other.n_rows), "The two matrices have different dimensions"
        except AssertionError as error:
            raise
        
        result = Matrix([[0],[0]])
        
        mat_1 = np.array(self.rows)
        mat_2 = np.array(other.rows)
        
        mat_3 = mat_1-mat_2
        
        result.rows = list(mat_3)
        result.n_cols = self.n_cols
        result.n_rows = self.n_rows
        result.det = result.calculate_det()
        
        return result
    
    
    def __mul__(self,other):
        
        """Magic method: ovverrides the usual behaviour of the "*" operator
        
        Args: -other(Matrix obj): the second matrix to be added
        
        Returns: the Matrix obj resulted from the product of the 2 starting ones
        """
        
        try:
            assert self.n_cols == other.n_rows, "The number of columns of the first matrix is not equal to the number of rows of the second one"
        except AssertionError as error:
            raise
        
        result = Matrix([[0],[0]])
        
        mat_1 = np.array(self.rows)
        mat_2 = np.array(other.rows)
        
        mat_3 = np.matmul(mat_1,mat_2)
        
        result.rows = list(mat_3)
        result.n_cols = other.n_cols
        result.n_rows = self.n_rows
        result.det = result.calculate_det()
        return result
        
    
    
    
    def __repr__(self):
        
        """Method to output the characteristics of the Matrix instance
        
        Args: None
        
        Returns: string with the informations
        """
        
        if self.n_rows == self.n_cols:
            return f"The matrix has {self.n_rows} rows, {self.n_cols} columns and determinant {self.det}"
        else:
            f"The matrix has {self.n_rows} rows, {self.n_cols} columns."
        
        
        
    
    














