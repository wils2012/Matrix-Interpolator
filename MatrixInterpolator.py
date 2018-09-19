import random
import warnings


inMatrix = [[random.randint(0,100) for x in range(0,50)] for y in range(0,50)]

pointArr = []
tupArr = []

###A function that accepts a row number, column number and a 2-D matrix and returns a list of tuples with the maximum
###adjacent product and the indices of the factors of that product
def findMaxProd(row, col, matrix):

    pointArr.clear()

    ########North Product########
    if (row - 3 >= 0):
        northProd = (matrix[row - 3][col] * matrix[row - 2][col] * matrix[row - 1][col] * matrix[row][col])
        pointArr.append((northProd, [(row,col), ((row-1),col), ((row-2),col), ((row-3),col)]))

    ########South Product########
    if (row + 3 <= (len(matrix)-1)):
        southProd = (matrix[row + 3][col] * matrix[row + 2][col] * matrix[row + 1][col] * matrix[row][col])
        pointArr.append((southProd,[(row,col), ((row+1),col), ((row+2),col), ((row+3),col)]))

    ########West Product########
    if ((col - 3) >= 0):
        westProd = (matrix[row][col - 3] * matrix[row][col - 2] * matrix[row][col - 1] * matrix[row][col])
        pointArr.append((westProd, [(row, col), (row, (col-1)), (row, (col-2)), (row, (col-3))]))

    ########East Product########
    if ((col + 3) <= (len(matrix[0]) - 1)):
        eastProd = (matrix[row][col + 3] * matrix[row][col + 2] * matrix[row][col + 1] * matrix[row][col])
        pointArr.append((eastProd, [(row, col), (row, (col+1)), (row, (col+2)), (row, (col+3))]))

    ########Northwest Product########
    if ((row - 3 >= 0) and (col - 3 >= 0)):
        nwProd = (matrix[row - 3][col - 3] * matrix[row - 2][col - 2] * matrix[row - 1][col - 1] * matrix[row][col])
        pointArr.append((nwProd, [(row, col), ((row-1), (col-1)), ((row-2), (col-2)), ((row-3), (col-3))]))

    ########Southwest Product########
    if ((row + 3 <= (len(matrix) - 1)) and (col - 3 >= 0)):
        swProd = (matrix[row + 3][col - 3] * matrix[row + 2][col - 2] * matrix[row + 1][col - 1] * matrix[row][col])
        pointArr.append((swProd, [(row, col), ((row+1), (col-1)), ((row+2), (col-2)), ((row+3), (col-3))]))

    ########Northeast Product########
    if ((row - 3 >= 0) and (col + 3) <= (len(matrix[0]) - 1)):
        neProd = (matrix[row - 3][col + 3] * matrix[row - 2][col + 2] * matrix[row - 1][col + 1] * matrix[row][col])
        pointArr.append((neProd,[(row, col), ((row-1), (col+1)), ((row-2), (col+2)), ((row-3), (col+3))]))

    ########Southeast Product########
    if ((row + 3 <= (len(matrix) - 1)) and (col + 3) <= (len(matrix[0]) - 1)):
        seProd = (matrix[row + 3][col + 3] * matrix[row + 2][col + 2] * matrix[row + 1][col + 1] * matrix[row][col])
        pointArr.append((seProd, [(row, col), ((row+1), (col+1)), ((row+2), (col+2)), ((row+3), (col+3))]))

    ###if point list is not empty, return tuple with the greatest product
    if pointArr:
        returnVal = max(pointArr)
        pointArr.clear()
        return returnVal



#Function that accepts an MxN matrix and returns a list of Tuples containing the
def matrixInterpolator(matrix):
    tupArr.clear()
    #Cycle through all indices and convert any strings or floats to ints
    for row, arr in enumerate(matrix):
        for col, index in enumerate(arr):
            if((type(matrix[row][col]) is float) or (type(matrix[row][col]) is str)):
                warnings.warn("str and float types will be converted to int types")
                matrix[row][col] = int(matrix[row][col])

    #Once all inputs are ints, cycle though each index, find maximum adjacent product, and add to output list of tuples
    for row, arr in enumerate(matrix):
        for col, index in enumerate(arr):
            tupArr.append(findMaxProd(row, col, matrix))

    return tupArr
