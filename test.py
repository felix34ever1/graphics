import matrix as m

m1 = m.Matrix(3,3,[6,3,2,8,7,7,1,1,1])
fun_list = m.matrixToVector(m1)
for element in fun_list:
    element.display()