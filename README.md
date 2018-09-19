# Matrix-Interpolator
Converting numeric 2-D matrix inputs into specific tuple output

## Additional Details
Contains a function which will take into it a M x N list of Integers (0, 100) and returns a Tuple containing a) the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) and b) A list of the indices of the numbers used as tuples of the format (row, column). Designed to accept M and N >= 4 and <= 50. If the Matrix contains a string or float and it will be converted to an int without any loss of precision but a warning will be printed acknowledging the type conversion.

## Getting Started

This function requires only the Python standard library. The function matrixInterpolator accepts a 2-D list and returns a list of tuples of the specifications listed in the Additional Details. A basic demonstration of the operation of this function can be shown by executing demo_MatrixInterpolator.py

## Running the tests

test_MatrixInterpolator.py contains a suite of 8 unit tests each designed to test the proper maximum is being calculated for a specific direction from one point in a matrix to its adjacent 3 points in that specific direction.  

## Authors

* **JosephVirgilio** - *Initial work* - [wils2012](https://github.com/wils2012)
