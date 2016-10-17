#Tool for checking linear dependence
from determinant import solve as det

#test = [(1,0,-1),(-2,1,1),(-1,2,-1)]
[(1,0),(0,1)]
def checkLinearDependence(arrTuples):
    for tup in arrTuples:
        if len(arrTuples[0]) != len(tup):
            return "Incompatible Vectors"
    if len(arrTuples) > len(arrTuples[0]):
        return "Linearly Dependent if each vector is represented as a column vector in a matrix the number of columns is greater than rows"
    elif len(arrTuples) == len(arrTuples[0]):
        if det(test,1) == 0:
            return "Linearly Dependent as determinant is zero"
        else:
            return "Linearly Independent as determinant is a non-zero"

test = eval(input("Enter vectors as an array: \n"))
val = checkLinearDependence(test)
print(str(val))
        