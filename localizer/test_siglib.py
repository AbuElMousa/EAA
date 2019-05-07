import unittest

import matplotlib.pyplot as plt

from siglib import sine
from siglib import get_signals
from siglib import calculate_mic_source_radii
from siglib import generate_noise
from siglib import generate_decay
from siglib import generate_delay

import numpy as np

mics = [
        {'id': 0, 'position': [1, 1], 'samples': None},
        {'id': 1, 'position': [1, -1], 'samples': None},
        {'id': 2, 'position': [-1, 1], 'samples': None},
        {'id': 3, 'position': [-1, -1], 'samples': None}
]

time = {'start': 0, 'end': 1}

sampling = {
        'number_of_samples': 1000,
        'c': 330
        }        


class SiglibTestCase(unittest.TestCase):
    pass


class TestPlotSignals(SiglibTestCase):
    def runTest(self):
        signals = get_signals(source_position=[6, 10], frequencies=[5, 10, 15, 20], samples=1024, c=330, start=0, end=1, noise=1)
        for sig in signals:
            plt.plot(sig)
        plt.show()
