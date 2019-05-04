import numpy as np
from numpy.fft import fft, fftfreq
from libpruio import *

import datetime

#kilosamples / sec
#6k is 166667
#12k is 83333
#24k is 41666 GOOD
#48k is 20833

NUM_SAMPLES = 1024

CHANNEL_0 = np.zeros(NUM_SAMPLES)
CHANNEL_1 = np.zeros(NUM_SAMPLES)
CHANNEL_2 = np.zeros(NUM_SAMPLES)

CHANNEL_0_FFT = np.zeros(NUM_SAMPLES)
CHANNEL_1_FFT = np.zeros(NUM_SAMPLES)
CHANNEL_2_FFT = np.zeros(NUM_SAMPLES)

io = pruio_new(PRUIO_DEF_ACTIVE, 0, 0, 0)
IO = io.contents
if  IO.Errr: raise AssertionError("pruio_new failed (%s)" % IO.Errr)

if pruio_config(io, NUM_SAMPLES, 0b11100, 166667, 0):
    raise AssertionError("config failed (%s)" % IO.Errr)

while True:
    if pruio_mm_start(io, 0, 0, 0, 0):
        raise AssertionError("mm_start failed (%s)" % IO.Errr)

    AdcV = IO.Adc.contents.Value

    for i in range(NUM_SAMPLES):
        CHANNEL_0[i] = AdcV[(i * 3)]
        CHANNEL_1[i] = AdcV[(i * 3) + 1]
        CHANNEL_2[i] = AdcV[(i * 3) + 2]


    CHANNEL_0_FFT = fft(CHANNEL_0)/NUM_SAMPLES
    CHANNEL_1_FFT = fft(CHANNEL_1)/NUM_SAMPLES
    CHANNEL_2_FFT = fft(CHANNEL_2)/NUM_SAMPLES

    CHANNEL_0_FFT[0] = 0
    CHANNEL_1_FFT[0] = 0
    CHANNEL_2_FFT[0] = 0

    CHANNEL_0_FREQS = fftfreq(len(CHANNEL_0_FFT), d=166667/1000000000.0)
    CHANNEL_1_FREQS = fftfreq(len(CHANNEL_1_FFT), d=166667/1000000000.0)
    CHANNEL_2_FREQS = fftfreq(len(CHANNEL_2_FFT), d=166667/1000000000.0)

    idx_0 = np.argmax(np.abs(CHANNEL_0_FFT))
    idx_1 = np.argmax(np.abs(CHANNEL_1_FFT))
    idx_2 = np.argmax(np.abs(CHANNEL_2_FFT))

    freq_0 = CHANNEL_0_FREQS[idx_0]
    freq_1 = CHANNEL_1_FREQS[idx_1]
    freq_2 = CHANNEL_2_FREQS[idx_2]

    freq_0 = abs(freq_0)
    freq_1 = abs(freq_1)
    freq_2 = abs(freq_2)

    print(round(freq_0), round(freq_1), round(freq_2))

pruio_destroy(io)
