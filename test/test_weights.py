import unittest
import numpy as np

from pymcdm import weights


class TestEqualWeights(unittest.TestCase):
    """ Test output method without reference (no needed) """

    def test_output(self):
        matrix = np.array([[1, 2, 3, 5],
                           [2, 3, 4, 8]])

        output = [0.25, 0.25, 0.25, 0.25]
        output_method = list(weights.equal_weights(matrix))

        self.assertListEqual(output, output_method)


class TestEntropyWeights(unittest.TestCase):
    """ Test output method with reference:
    [1] Elsayed, Elsayed A., A. Shaik Dawood, and R. Karthikeyan. "Evaluating alternatives through the application of
    TOPSIS method with entropy weight." Int. J. Eng. Trends Technol 46.2 (2017): 60-66.
    """

    def test_output(self):

        matrix = np.array([[7, 312, 1891, 6613, 163],
                           [72, 88, 728, 941804, 1078],
                           [10, 252, 2594, 3466, 117471],
                           [10, 145, 980, 2371, 86329],
                           [65, 54, 350, 501, 29897],
                           [29, 48, 380, 912, 34051],
                           [7, 476, 3300, 78470, 2212],
                           [70, 87, 650, 733, 819000],
                           [4, 86, 591, 3015, 103],
                           [12, 79, 579, 3240, 96098],
                           [21, 45, 261, 1253, 453],
                           [1, 72, 530, 4333, 0.104800]])

        output = [0.104991, 0.069124, 0.071373, 0.449937, 0.304575]
        output_method = [round(weight, 6) for weight in weights.entropy_weights(matrix)]

        self.assertListEqual(output, output_method)
