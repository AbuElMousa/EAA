import unittest

from jlib import build_TOA_matrix
from jlib import compute_direction
from jlib import x_correlation

from siglib import get_samples

import numpy as np

print(get_samples())
exit()

mics = [
        {'id': 0, 'position': [1, 1], 'samples': sine()},
        {'id': 1, 'position': [1, -1], 'samples': sine()},
        {'id': 2, 'position': [-1, 1], 'samples': sine()},
        {'id': 3, 'position': [-1, -1], 'samples': sine()}
]

time = {'start': 0, 'end': 1}

sampling = {
        'number_of_samples': 1000,
        'c': 330
        }

# ACTUAL TESTING

#mat = build_TOA_matrix(mics, time, sampling)
#print(mat)
direction = compute_direction([[0, .004, .004, .007]], mics, sampling)
print(direction)

'''
get the
'''

#print(mics)
class TOATestCase(unittest.TestCase):
    def setUp(self):
        self.something = 1

    def tearDown(self):
        pass


class TOATest(TOATestCase):
    def runTest(self):
        assert 1 == 1

#class CorrelateTestCase()

