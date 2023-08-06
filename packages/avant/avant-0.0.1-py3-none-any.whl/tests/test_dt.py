
import unittest
import numpy as np
from numpy.testing import assert_almost_equal
from ..parameter.gauss_class import Gauss
from ..parameter import dt as dt


class TestDt(unittest.TestCase):

    def test_Gauss(self):
        a = dt.Gauss('DMPC')
        loc_scale = np.atleast_2d([(27.96,0.3), (29.0,2.0), (28.0,0.6)])
        b = Gauss(loc_scale, 10.0, 50.0)
        assert_almost_equal(a.pdf(0.5), b.pdf(0.5))

    def test_uniform(self):
        b = dt.uniform('DMPC')
        assert_almost_equal(b, np.array([[10.0, 50.0]]))
