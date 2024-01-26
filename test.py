import vector as v
import matrix as m
import shape

cube = shape.Shape()
cube.setVertices([
    v.Vector3D(75,75,0), #0
    v.Vector3D(75,125,0),#1
    v.Vector3D(125,125,0),#2
    v.Vector3D(125,75,0),#3
    v.Vector3D(75,75,-10),#4
    v.Vector3D(75,125,-10),#5
    v.Vector3D(125,125,-10),#6
    v.Vector3D(125,75,-10)#7
])

cube.setSurfaces( #just defined the connections of a cube
    [[0,1,2,3],[0,1,5,4],[3,2,6,7],[0,3,7,4],[1,2,6,5],[4,5,6,7]]
)

v1 = cube.vertices[0]
v2 = cube.vertices[1]
v.sub(v1,v2).display()