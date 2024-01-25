class Vector3D():
    '''Defines a vector with 3 dimensions to be used for points in 3d shapes.'''

    def __init__(self,x:int,y:int,z:int) -> None:
        '''Takes x,y,z position coordinates (pixels where topleft of screen is 0,0)'''
        self.x,self.y,self.z = x,y,z

    def display(self):
        print(f"{self.x}\n{self.y}\n{self.z}\n")