
# Define Matrix class and matrix operations that can be called outside of a matrix

class Matrix():
    '''Defines a matrix(represented by a 2D array) with functions to be able to manipulate it'''
    


    def __init__(self,num_rows:int,num_cols:int,numbers:list[int] = None):
        ''' Create a matrix by giving row number and column number for dimensions and a list of numbers which will be put in row order.
        If numbers is left empty, it will create a zero matrix.'''
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.array:list[list] = []
        if numbers!=None:
            self.array = []
            for i in range(num_rows):
                self.array.append([])
                for j in range(num_cols):
                    self.array[i].append(numbers[i*self.num_cols+j])
        else:
            for i in range(num_rows):
                self.array.append([])
                for j in range(num_cols):
                    self.array[i].append(0)

    def display(self)->None:
        for i in range(self.num_rows):
            new_string = ""
            for j in range(self.num_cols):
                new_string+=str(self.array[i][j])+" "
            print(new_string)
    
    def getCol(self,row_index)->list[int]:
        return(self.array[row_index])

def add(m1:Matrix,m2:Matrix)->Matrix:
    if m1.num_rows == m2.num_rows and m1.num_cols == m2.num_cols:
        new_matrix = Matrix(m1.num_rows,m1.num_cols)
        for i in range(m1.num_rows):
            for j in range(m1.num_cols):
                new_matrix.array[i][j] = m1.array[i][j]+m2.array[i][j]
        return new_matrix
    else:
        new_matrix = Matrix(1,1,[0])
        return(new_matrix)

def multiply(m1:Matrix,m2:Matrix)->Matrix:
    if m1.num_cols == m2.num_rows:
        new_matrix = Matrix(m1.num_rows,m2.num_cols)
        for i in range(m1.num_rows):
            for j in range(m2.num_cols):
                total = 0
                for k in range(m1.num_cols): # Add up all numbers and multiply
                    total+=m1.array[i][k]*m2.array[k][j]
                new_matrix.array[i][j] = total
        return new_matrix
    else:
        new_matrix = Matrix(1,1,[0])
        return(new_matrix)        

        
    
def matrixToVector3D(m1:Matrix):
    '''Returns a list of Vector3Ds from any array which has a column size >= 3. If greater, only the first 3 values will be taken. '''
    if len(m1.array[0]) >= 3:
        vector_list = []
        for i in range(len(m1.array)):
            data = m1.array[i]
            vector_list.append(vector.Vector3D(data[0],data[1],data[2]))
        return vector_list
    else:
        return vector.Vector3D(0,0,0)


import vector