import unittest
import numpy as np

from pymcdm import normalizations as norm


class TestMinmaxNormalization(unittest.TestCase):
    """ Test output method without reference """

    def test_output(self):
        matrix = np.array([[66, 56, 95],
                           [61, 55, 166],
                           [65, 49, 113],
                           [95, 56, 99],
                           [63, 43, 178],
                           [74, 59, 140]])

        types = np.array([-1, -1, 1])
        output = [0.85294118, 0.1875, 0.0, 1.0, 0.25, 0.85542169, 0.88235294, 0.625, 0.21686747, 0.0, 0.1875,
                  0.04819277, 0.94117647, 1.0, 1.0, 0.61764706, 0.0, 0.54216867]

        output_method = norm.normalize_matrix(matrix, norm.minmax_normalization, types).reshape(-1)
        output_method = [round(val, 8) for val in output_method]
        self.assertListEqual(output, output_method)


class TestMaxNormalization(unittest.TestCase):
    """ Test output method without reference """

    def test_output(self):
        matrix = np.array([[66, 56, 95],
                           [61, 55, 166],
                           [65, 49, 113],
                           [95, 56, 99],
                           [63, 43, 178],
                           [74, 59, 140]])

        types = np.array([-1, -1, 1])
        output = [0.30526316, 0.05084746, 0.53370787, 0.35789474, 0.06779661, 0.93258427, 0.31578947, 0.16949153,
                  0.63483146, 0.0, 0.05084746, 0.55617978, 0.33684211, 0.27118644, 1.0, 0.22105263, 0.0, 0.78651685]

        output_method = norm.normalize_matrix(matrix, norm.max_normalization, types).reshape(-1)
        output_method = [round(val, 8) for val in output_method]
        self.assertListEqual(output, output_method)


class TestSumNormalization(unittest.TestCase):
    """ Test output method without reference """

    def test_output(self):
        matrix = np.array([[66, 56, 95],
                           [61, 55, 166],
                           [65, 49, 113],
                           [95, 56, 99],
                           [63, 43, 178],
                           [74, 59, 140]])

        types = np.array([-1, -1, 1])
        output = [0.17447136, 0.155945, 0.12010114, 0.1887723, 0.15878037, 0.20986094, 0.17715554, 0.17822286,
                  0.14285714, 0.12121168, 0.155945, 0.12515803, 0.18277952, 0.20309117, 0.22503161, 0.15560959,
                  0.1480156, 0.17699115]

        output_method = norm.normalize_matrix(matrix, norm.sum_normalization, types).reshape(-1)
        output_method = [round(val, 8) for val in output_method]
        self.assertListEqual(output, output_method)


class TestVectorNormalization(unittest.TestCase):
    """ Test output method without reference """

    def test_output(self):
        matrix = np.array([[66, 56, 95],
                           [61, 55, 166],
                           [65, 49, 113],
                           [95, 56, 99],
                           [63, 43, 178],
                           [74, 59, 140]])

        types = np.array([-1, -1, 1])
        output = [0.62375904, 0.57085288, 0.28587109, 0.65226214, 0.57851622, 0.49952212, 0.62945966, 0.62449627,
                  0.34003614, 0.45844104, 0.57085288, 0.29790777, 0.6408609, 0.67047632, 0.53563215, 0.57815408,
                  0.54786285, 0.42128371]

        output_method = norm.normalize_matrix(matrix, norm.vector_normalization, types).reshape(-1)
        output_method = [round(val, 8) for val in output_method]
        self.assertListEqual(output, output_method)