import random
import MatrixInterpolator

inMatrix = [[random.randint(0,100) for x in range(0,50)] for y in range(0,50)]

print(MatrixInterpolator.matrixInterpolator(inMatrix))