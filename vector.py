class Vector3D():
    '''Defines a vector with 3 dimensions to be used for points in 3d shapes.'''

    def __init__(self,x:int,y:int,z:int) -> None:
        '''Takes x,y,z position coordinates (pixels where topleft of screen is 0,0)'''
        self.x,self.y,self.z = x,y,z

    def display(self):
        print(f"{self.x}\n{self.y}\n{self.z}\n")


def add(v1:Vector3D,v2:Vector3D)->Vector3D:
    return Vector3D(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)

def sub(v1:Vector3D,v2:Vector3D)->Vector3D:
    return Vector3D(v1.x-v2.x,v1.y-v2.y,v1.z-v2.z)

def dotProduct(v1:Vector3D,v2:Vector3D):
    return (v1.x*v2.x+v1.y*v2.y+v1.z*v2.z)