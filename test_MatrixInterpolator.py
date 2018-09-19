import unittest
import MatrixInterpolator


class TestStringMethods(unittest.TestCase):

    eastMatrix = [[2,2,2,2],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    westMatrix = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[3,3,3,3]]
    northMatrix = [[4,1,1,1],[4,1,1,1],[4,1,1,1],[4,1,1,1]]
    southMatrix = [[1,1,1,5],[1,1,1,5],[1,1,1,5],[1,1,1,5]]
    neMatrix = [[1,1,1,6],[1,1,6,1],[1,6,1,1],[6,1,1,1]]
    seMatrix = [[7,1,1,1],[1,7,1,1],[1,1,7,1],[1,1,1,7]]
    nwMatrix = [[8,1,1,1],[1,8,1,1],[1,1,8,1],[1,1,1,8]]
    swMatrix = [[1,1,1,9],[1,1,9,1],[1,9,1,1],[9,1,1,1]]


    def test_east(self):
        self.assertEqual((MatrixInterpolator.findMaxProd(0, 0, self.eastMatrix))[0], 16)

    def test_west(self):
        self.assertEqual((MatrixInterpolator.findMaxProd(3, 3, self.westMatrix))[0], 81)

    def test_north(self):
        self.assertEqual((MatrixInterpolator.findMaxProd(3, 0, self.northMatrix))[0], 256)

    def test_south(self):
        self.assertEqual((MatrixInterpolator.findMaxProd(0, 3, self.southMatrix))[0], 625)

    def test_ne(self):
        self.assertEqual((MatrixInterpolator.findMaxProd(3, 0, self.neMatrix))[0], 1296)

    def test_se(self):
        self.assertEqual((MatrixInterpolator.findMaxProd(0, 0, self.seMatrix))[0], 2401)

    def test_nw(self):
        self.assertEqual((MatrixInterpolator.findMaxProd(3, 3, self.nwMatrix))[0], 4096)

    def test_sw(self):
        self.assertEqual((MatrixInterpolator.findMaxProd(0, 3, self.swMatrix))[0], 6561)


if __name__ == '__main__':
    unittest.main()
