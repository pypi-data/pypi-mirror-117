
import unittest
import numpy as np
from numpy.testing import assert_almost_equal
from ..parameter.gauss_class import Gauss
from ..parameter import roughness as r


class TestRoughness(unittest.TestCase):

    def test_Gauss(self):
        a = r.Gauss('DMPC')
        loc_scale = np.atleast_2d([(4.42,0.16), (3.9,0.6), (2.5,0.5),(3.02,0.08),(5.0,2.0),(3.3,0.4)])
        b = Gauss(loc_scale, 0.0, 10.0)
        assert_almost_equal(a.pdf(0.5), b.pdf(0.5))

    def test_uniform(self):
        b = r.uniform('DMPC')
        assert_almost_equal(b, np.array([[0.0, 10.0]]))