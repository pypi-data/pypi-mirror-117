#import sys
#sys.path.append('../')

import unittest
import numpy as np
from numpy.testing import assert_equal, assert_almost_equal
from ..parameter.gauss_class import Gauss
from ..parameter.util import findGauss, findUniform

loc_scale = np.atleast_2d([(320.9, 20.1), (339.5, 14.5),(319.0,6.0)])
test_gauss = Gauss(loc_scale, 250.0, 450.0)

class TestUtil(unittest.TestCase):

    def test_findGauss(self):
        a = findGauss('DMPC','v_h')
        assert_almost_equal(a.pdf(0.5),test_gauss.pdf(0.5))

    def test_findUniform(self):
        b = findUniform('DMPC','v_h')
        assert_almost_equal(b,np.array([[250.0,450.0]]))