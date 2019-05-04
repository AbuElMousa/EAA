from __future__ import division
import bisect
import numpy as np
from scipy.spatial import distance
from scipy.signal import correlate, hilbert


def x_correlation(mic_data, time_data, sampling_data, TOA):
    """Computes the cross correlation in time across all available channels.

    Computes the cross correlation in time across all available channels.

    ===============================================================================================
    :param mic_data: a list of dictionaries with input information for the current iteration
    :param time_data: a dictionary with the start and end time of the smapling
    :param sampling: a dictionary containing the number of samples and speed of sound
    :return: The cross correlation values of all the combinations
    """
    number_of_samples = sampling_data['number_of_samples']
    start = time_data['start']
    end = time_data['end']

    input_signals = [mic['samples'] for mic in mic_data]
    num_mics = len(input_signals)
    matlist = []
    matlist1 = []
    for i in range(num_mics):
        tmp = []
        tmp1 = []
        for j in range(num_mics):
            mean_int = 10
            mic_i_convolve = input_np.convolve(input_signals[i], np.ones((mean_int,))/mean_int, mode='valid')
            mic_j_convolve = input_np.convolve(input_signals[j], np.ones((mean_int,))/mean_int, mode='valid')
            x_correlate = correlate(mic_i_convolve, mic_j_convolve, mode='full')
            x_correlate_length = len(x_correlate)
            x_correlate_envelope = np.abs(abs(hilbert(x_correlate)))
            x_correlate_max_x_position = np.argmax(x_correlate_envelope)

            t_correlate = np.linspace(0, len(x_correlate) - 1, num=len(x_correlate))
            t_correlate_center = len(t_correlate) / 2.0

            t_correlate = t_correlate - np.ones(len(t_correlate)) * t_correlate_center

            p = bisect.bisect(t_correlate, TOA.item(i, j))
            tmp1.append(p)
            tmp.append(x_correlate_max_x_position)
        matlist.append(templist)
        matlist1.append(templist1)
    x_correlate_matrix = np.matrix(matlist)
    t_correlate_matrix = np.matrix(matlist1)
    sub_s = np.subtract(x_correlate_matrix, t_correlate_matrix)
    min_row = sub_s.min(0)
    sub_s = np.subtract(sub_s.(0), float(min_row.min()))
    sub_s = np.divide(sub_s, (number_of_samples / (end - start)))
    return sub_s

    

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

#mat = build_TOA_matrix(mics, time, sampling)
#print(mat)
direction = compute_direction([[0, .004, .004, .007]], mics, sampling)
print(direction)

'''
get the 
'''

#print(mics)
