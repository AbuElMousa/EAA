import unittest

from jlib import build_TOA_matrix
from jlib import compute_direction
from jlib import x_correlation

from siglib import get_signals

import numpy as np

###############################################################################
################################## FUNCTIONS ##################################
###############################################################################

signal = get_signals()

mics = [
        {'id': 0, 'position': [1, 1], 'samples': signal[0]},
        {'id': 1, 'position': [1, -1], 'samples': signal[1]},
        {'id': 2, 'position': [-1, 1], 'samples': signal[2]},
        {'id': 3, 'position': [-1, -1], 'samples': signal[3]}
]

time = {'start': 0, 'end': 1}

sampling = {
        'number_of_samples': 1000,
        'c': 330
        }

###############################################################################
#################################### TESTS ####################################
###############################################################################


class EstimationTest(unittest.TestCase):
    pass


class EstimateBlah(EstimationTest):
    def runTest(self):
        mic_data = mics
        time_data = time
        sampling_data = sampling
        TOA = build_TOA_matrix(mic_data, time_data, sampling_data)
        minimum_time_row = x_correlation(mic_data, time_data, sampling_data, TOA)
        direction = compute_direction(minimum_time_row, mic_data, sampling_data)       
        print(direction)
