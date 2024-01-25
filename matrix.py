# Define Matrix class and matrix operations that can be called outside of a matrix

class Matrix():
    '''Defines a matrix(represented by a 2D array) with functions to be able to manipulate it'''
    


    def __init__(self,row_size:int,column_size:int,numbers:list[int] = None):
        ''' Create a matrix by giving row number and column number for dimensions and a list of numbers which will be put in column order.
        If numbers is left empty, it will create a zero matrix.'''
        self.row_size = row_size
        self.column_size = column_size
        self.array = []
        if type(numbers)!=None:
            self.array = []
            for i in range(row_size):
                self.array.append([])
                for j in range(column_size):
                    self.array[i].append(0)
        else:
            for i in range(row_size):
                self.array.append([])
                for j in range(column_size):
                    self.array[i].append(numbers[i*self.row_size+j])

    def display(self)->None:
        for i in range(self.column_size):
            new_string = ""
            for j in range(self.row_size):
                new_string+=str(self.array[j][i])+" "
            print(new_string)