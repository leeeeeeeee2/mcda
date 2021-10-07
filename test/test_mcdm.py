import unittest
import numpy as np

from pymcdm import methods
from pymcdm.methods.mcda_method import MCDA_method


class TestMCDA(unittest.TestCase):

    def test_validation(self):
        with self.assertRaises(ValueError):
            body = MCDA_method()
            matrix = np.array([[1, 2, 3], [1, 2, 3]])
            weights = np.array([0.5, 0.5])
            types = np.array([1, -1, -1])
            body(matrix, weights, types)


class TestARAS(unittest.TestCase):
    """ Test output method with reference:
    [1] Stanujkic, D., Djordjevic, B., & Karabasevic, D. (2015). Selection of
    candidates in the process of recruitment and selection of personnel based on the SWARA and ARAS methods.
    Quaestus, (7), 53.
    """

    def test_output(self):
        with self.assertRaises(ValueError):
            body = methods.ARAS()
            matrix = np.array([[4.64, 3.00, 3.00, 3.00, 2.88, 3.63],
                               [4.00, 4.00, 4.64, 3.56, 3.63, 5.00],
                               [3.30, 4.31, 3.30, 4.00, 3.30, 4.00],
                               [2.62, 5.00, 4.22, 4.31, 5.00, 5.00]])

            weights = np.array([0.28, 0.25, 0.19, 0.15, 0.08, 0.04])
            types = np.array([1, 1, 1, 1, 1, 1])

            output = np.array([0.74, 0.86, 0.78, 0.86])

            if output != body(matrix, weights, types):
                raise ValueError('Output not equal with reference!')
