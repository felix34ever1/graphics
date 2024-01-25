
# Define Matrix class and matrix operations that can be called outside of a matrix

class Matrix():
    '''Defines a matrix(represented by a 2D array) with functions to be able to manipulate it'''
    


    def __init__(self,row_size:int,column_size:int,numbers:list[int] = None):
        ''' Create a matrix by giving row number and column number for dimensions and a list of numbers which will be put in column order.
        If numbers is left empty, it will create a zero matrix.'''
        self.row_size = row_size
        self.column_size = column_size
        self.array:list[list] = []
        if numbers!=None:
            self.array = []
            for i in range(row_size):
                self.array.append([])
                for j in range(column_size):
                    self.array[i].append(numbers[i*self.column_size+j])
        else:
            for i in range(row_size):
                self.array.append([])
                for j in range(column_size):
                    self.array[i].append(0)

    def display(self)->None:
        for i in range(self.column_size):
            new_string = ""
            for j in range(self.row_size):
                new_string+=str(self.array[j][i])+" "
            print(new_string)
    
    def getCol(self,row_index)->list[int]:
        return(self.array[row_index])

def add(m1:Matrix,m2:Matrix)->Matrix:
    if m1.row_size == m2.row_size and m1.column_size == m2.column_size:
        new_matrix = Matrix(m1.row_size,m1.column_size)
        for i in range(m1.row_size):
            for j in range(m1.column_size):
                new_matrix.array[i][j] = m1.array[i][j]+m2.array[i][j]
        return new_matrix
    else:
        return([[0]])
    
def matrixToVector(m1:Matrix):
    '''Returns a list of Vector3Ds '''
    if len(m1.array[0]) == 3:
        vector_list = []
        for i in range(len(m1.array)):
            data = m1.array[i]
            vector_list.append(vector.Vector3D(data[0],data[1],data[2]))
        return vector_list
    else:
        return vector.Vector3D(0,0,0)


import vector