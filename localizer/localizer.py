import numpy as np
from numpy.fft import fft, fftfreq
from libpruio import *
from jlib import build_TOA_matrix, compute_direction, x_correlation 
from configuration import mic_configuration, time_configuration, sampling_configuration

import datetime

NUM_SAMPLES = 1024
FREQUENCY_RANGE = range(0, 3000)
TOA = build_TOA_matrix(mic_configuration, time_configuration, sampling_configuration)
print(TOA)

CHANNEL_0 = np.zeros(NUM_SAMPLES)
CHANNEL_1 = np.zeros(NUM_SAMPLES)
CHANNEL_2 = np.zeros(NUM_SAMPLES)
CHANNEL_3 = np.zeros(NUM_SAMPLES)

mic_configuration[0]['samples'] = CHANNEL_0
mic_configuration[1]['samples'] = CHANNEL_1
mic_configuration[2]['samples'] = CHANNEL_2
mic_configuration[3]['samples'] = CHANNEL_3

CHANNEL_0_FFT = np.zeros(NUM_SAMPLES)
CHANNEL_1_FFT = np.zeros(NUM_SAMPLES)
CHANNEL_2_FFT = np.zeros(NUM_SAMPLES)
CHANNEL_3_FFT = np.zeros(NUM_SAMPLES)

io = pruio_new(PRUIO_DEF_ACTIVE, 0, 0, 0)
IO = io.contents
if  IO.Errr: raise AssertionError("pruio_new failed (%s)" % IO.Errr)

if pruio_config(io, NUM_SAMPLES, 0b11110, 166667, 0):
    raise AssertionError("config failed (%s)" % IO.Errr)

while True:
    if pruio_mm_start(io, 0, 0, 0, 0):
        raise AssertionError("mm_start failed (%s)" % IO.Errr)

    AdcV = IO.Adc.contents.Value

    for i in range(NUM_SAMPLES):
        CHANNEL_0[i] = AdcV[(i * 4)]
        CHANNEL_1[i] = AdcV[(i * 4) + 1]
        CHANNEL_2[i] = AdcV[(i * 4) + 2]
        CHANNEL_3[i] = AdcV[(i * 4) + 3]

    CHANNEL_0_FFT = fft(CHANNEL_0)/NUM_SAMPLES
    CHANNEL_1_FFT = fft(CHANNEL_1)/NUM_SAMPLES
    CHANNEL_2_FFT = fft(CHANNEL_2)/NUM_SAMPLES
    CHANNEL_3_FFT = fft(CHANNEL_3)/NUM_SAMPLES

    CHANNEL_0_FFT[0] = 0
    CHANNEL_1_FFT[0] = 0
    CHANNEL_2_FFT[0] = 0
    CHANNEL_3_FFT[0] = 0

    CHANNEL_0_FREQS = fftfreq(len(CHANNEL_0_FFT), d=166667/1000000000.0)
    CHANNEL_1_FREQS = fftfreq(len(CHANNEL_1_FFT), d=166667/1000000000.0)
    CHANNEL_2_FREQS = fftfreq(len(CHANNEL_2_FFT), d=166667/1000000000.0)
    CHANNEL_3_FREQS = fftfreq(len(CHANNEL_3_FFT), d=166667/1000000000.0)

    idx_0 = np.argmax(np.abs(CHANNEL_0_FFT))
    idx_1 = np.argmax(np.abs(CHANNEL_1_FFT))
    idx_2 = np.argmax(np.abs(CHANNEL_2_FFT))
    idx_3 = np.argmax(np.abs(CHANNEL_3_FFT))

    freq_0 = CHANNEL_0_FREQS[idx_0]
    freq_1 = CHANNEL_1_FREQS[idx_1]
    freq_2 = CHANNEL_2_FREQS[idx_2]
    freq_3 = CHANNEL_3_FREQS[idx_3]

    freq_0 = abs(freq_0)
    freq_1 = abs(freq_1)
    freq_2 = abs(freq_2)
    freq_3 = abs(freq_3)

    for freq in [freq_0, freq_1, freq_2, freq_3]:
        print(freq)
        if int(freq) in FREQUENCY_RANGE:
            minimum_time_row = x_correlation(mic_configuration, time_configuration, sampling_configuration, TOA)
            direction = compute_direction(minimum_time_row, mic_configuration, sampling_configuration)
            print(direction)
            break

pruio_destroy(io)
