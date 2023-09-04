import numpy as np

ListA,ListB,ListC = [1,2,3],[4,5,6],[7,8,9]
Int1,Int2,Int3 = 1,2,3
Num1,Num2 = 4,5


#Matrix Creation
matrix = np.array([ListA,ListB,ListC]) #all lists must be same length
Mat1 = matrix = np.zeros(Int1,Int2) # Makes Int1 by Int2 matrix full of zeros
Mat2 = matrix = np.ones(Int1,Int2) # Makes matrix of ones
matrix = np.linspace(Num1,Num2,Int1) #creates a matrix of equally spaced elements between 'NumA' and 'NumB'
matrix = np.arrange(Int1).reshape(Int2,Int3) #Iterates through each element of IntA, in formation IntB,IntC matrix
matrix = np.func1(Mat1) #Applies the function to all elements of MatA
rg = np.random.default_rng(1) # Used as a random generator
matrix = rg.randon((2,3)) #Produces random elements between 0-1
    
Mat1 * Mat2 #Element multiplication
Mat1 @ Mat2 #Matrix multiplication
Mat1.sum() #Sums all the elements in the matrix
Mat1.cumsum()
Mat1.max(axis=0) #Max of each column
Mat1.min(axis=1) #Min of each row

matrix[2,3] #Outputs the element in row 2 column 3
matrix[0:5,1] #Outputs column 1 in rows 0-4
matrix[:,2] #Outputs column 2 in all rows
matrix[2,...] #Outputs same as matrix[2,:,:,:,...]

for row in matrix: #Iterates through the first axis of the matrix
    pass
for element in matrix.flat: #iterates through the elements
    pass

matrix.ndim # Number of dimensions of the array
matrix.shape # Returns a Tuple with row and column 
matrix.size # Returns the total number of elements
