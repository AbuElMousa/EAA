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


def compute_direction(minimum_time_row, mic_data, sampling_data):
    """Calculates the direction
    """
    c = sampling_data['c']
    mics = [mic['id'] for mic in mic_data]

    min_position = np.argmin(minimum_time_row)
    #initial_position = mic[min_position]['position']
    initial_position = mic_data[0]['position']
    delta_positions = [] #what does this mean

    for mic in mic_data:
        mic_position = mic['position']
        if mic_position != initial_position:
            delta = np.subtract(mic_position, initial_position)
            delta_positions.append(delta)

    delta_positions_matrix = np.matrix(delta_positions) # make sure this works properly
    pseudo_inverse = np.linalg.pinv(delta_positions_matrix)

    delta_time_matrix = [np.delete(minimum_time_row, min_position)] #why
    delta_time_matrix = np.multiply(delta_time_matrix, c)
    delta_time_matrix = np.transpose(delta_time_matrix)
    uv = np.dot(pseudo_inverse, delta_time_matrix)
    theta = np.arctan2(uv[1], uv[0]) # make this nicer
    theta = np.rad2deg(theta)

    if theta < 0:
        theta = theta + 180
    elif theta >= 0:
        theta = theta - 180

    direction = theta.min()

    return direction


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
    sub_s = np.subtract(sub_s(0), float(min_row.min()))
    sub_s = np.divide(sub_s, (number_of_samples / (end - start)))
    return sub_s
