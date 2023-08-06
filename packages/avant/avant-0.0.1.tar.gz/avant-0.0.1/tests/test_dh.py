
import unittest
import numpy as np
from numpy.testing import assert_almost_equal
from ..parameter.gauss_class import Gauss
from ..parameter import dh as dh

class TestDh(unittest.TestCase):

    def test_Gauss(self):
        a = dh.Gauss('DMPC')
        loc_scale = np.atleast_2d([(8.0, 1.0), (9.5, 1.6), (8.4, 1.1), (9.0,2.0)])
        b = Gauss(loc_scale, 4.0, 22.0)
        assert_almost_equal(a.pdf(0.5),b.pdf(0.5))

    def test_uniform(self):
        b = dh.uniform('DMPC')
        assert_almost_equal(b,np.array([[4.0,22.0]]))









