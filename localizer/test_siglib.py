import unittest

from siglib import sine
from siglib import get_signals
from siglib import calculate_mic_source_radii
from siglib import generate_noise
from siglib import generate_decay
from siglib import generate_delay

import numpy as np

'''
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
'''

# ACTUAL TESTING

'''
get the
'''

#print(mics)
class SiglibTestCase(unittest.TestCase):
    pass


class TestGetSignals(SiglibTestCase):
    def runTest(self):
        print(get_signals())

#class CorrelateTestCase()

