import unittest
import numpy as np
from numpy.testing import assert_almost_equal
from ..parameter.gauss_class import Gauss
from ..parameter import vt as vt


class TestVt(unittest.TestCase):

    def test_Gauss(self):
        a = vt.Gauss('DMPC')
        loc_scale = np.atleast_2d([(851.5,5.0), (815.9,15.5)])
        b = Gauss(loc_scale, 700.0, 1000.0)
        assert_almost_equal(a.pdf(0.5), b.pdf(0.5))

    def test_uniform(self):
        b = vt.uniform('DMPC')
        assert_almost_equal(b, np.array([[700.0, 1000.0]]))