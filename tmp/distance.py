from __future__ import division
import bisect
import numpy as np
from scipy.spatial import distance
from scipy.signal import correlate, hilbert

def build_TOA_matrix(mic_data, time_data, sampling_data):
    """Builds the Time of Arrival matrix for the given input

    Builds a matrix with the amount of time it takes to get from one matrix to another a the
    speed of sound.

    scipy.spatial.distance.euclidean: computes the euclidean distance betw. 2 1d arrays
    :param u: input array 1
    :param v: input array 2
    :return: the euclidean distance between vectors u and v

    ===============================================================================================
    :param mic_data: a list of dictionaries with input information for the current iteration
    :param time_data: a dictionary with the start and end time of the smapling
    :param sampling: a dictionary containing the number of samples and speed of sound
    :return: The TOA matrix
    """
    start = time_data['start']
    end = time_data['end']
    number_of_samples = sampling_data['number_of_samples']
    c = sampling_data['c']

    TOA = []
    for current_mic in mics:

        current_mic_position = current_mic['position']
        current_mic_toa = []

        for alt_mic in mics:

            alt_mic_position = alt_mic['position']

            time_delta = end - start
            samples_over_duration = number_of_samples / time_delta 
            inv_samples_over_duration = 1 / samples_over_duration
            mic_to_mic_dist = distance.euclidean(current_mic_position, alt_mic_position)
            current_mic_toa.append(mic_to_mic_dist / (inv_samples_over_duration * c))

        TOA.append(current_mic_toa)

    return TOA


def x_correlation(mic_data, time_data, sampling_data):
    """Computes the cross correlation in time across all available channels.

    Computes the cross correlation in time across all available channels.

    ===============================================================================================
    :param mic_data: a list of dictionaries with input information for the current iteration
    :param time_data: a dictionary with the start and end time of the smapling
    :param sampling: a dictionary containing the number of samples and speed of sound
    :return: The cross correlation values of all the combinations
    """
    input_signals = [mic['samples'] for mic in mic_data]
    matlist = []
    matlist1 = []
    for current_mic in 


# TEST FUNCTIONS
def sine():
    time = np.linspace(0, 1, 1000)
    phase = 0
    signal = np.sin(2 * np.pi * 440 * time + phase)
    return signal

# TEST DATA


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

mat = build_TOA_matrix(mics, time, sampling)
print(mat)


#print(mics)
