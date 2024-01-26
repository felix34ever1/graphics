import matrix as m
import vector as v

class Shape():

    def __init__(self,offset_x,offset_y) -> None:
        self.vertices:list[v.Vector3D]
        '''List of vertices that the shape contains'''
        self.surfaces:list[int] 
        '''Each surface is represented by a list of integers where each int is the index of the vertex in vertices list'''
        self.offset_x = offset_x
        self.offset_y = offset_y

    def setVertices(self,vertex_list:list[v.Vector3D]):
        self.vertices = vertex_list
    
    def setSurfaces(self,surface_list:list[list]):
        ''' Takes a list of lists which are the indexes of the vertices representing that surface.'''
        self.surfaces = surface_list

    def getVertex(self,index:int)->v.Vector3D:
        '''Get vertex by index from vertices list'''
        if index<len(self.vertices):
            return(self.vertices[index])
        else:
            return(v.Vector3D(0,0,0))
        
    def getSurfaceCoordinates(self,surface_index,camera_position:v.Vector3D)->list[list[int]]:
        '''returns a list of lists containing x and y coordinates'''
        surface = self.surfaces[surface_index]
        coordinates = []
        for vertex_index in surface:
            vertex = self.getVertex(vertex_index)
            # Now translate coordinates around the origin, perform algorithm and move them back
            try:
                #   v.Vector3D(-5,-5,-1), #0
                #   camera_position = v.Vector3D(0,0,-1)


                x = (((vertex.x-camera_position.x)*(vertex.z-camera_position.z))//vertex.z) # Applies algorithm learned in lecture
                # I had to guess some parts e.g x on slide = dx, zs on slide = abs(zs)
                x += camera_position.x+300
            except ZeroDivisionError: # Incase the position of the shape is zero, this is wrong and screws with the visuals
                x = vertex.x+100-camera_position.x
            try:
                y = ((vertex.y-camera_position.y)*(vertex.z-camera_position.z))//vertex.z # same but for y
                y+=camera_position.y+300
            except ZeroDivisionError: # Incase the position of the shape is zero, this is wrong and screws with the visuals
                y = vertex.y+100-camera_position.y

            coordinates.append([x,y])
        return(coordinates)