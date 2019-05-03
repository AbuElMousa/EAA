import numpy as np
from numpy.fft import fft, fftfreq
from libpruio import *

import datetime

NUM_SAMPLES = 1000 

CHANNEL_1 = np.zeros(NUM_SAMPLES)

CHANNEL_1_FFT = np.zeros(NUM_SAMPLES)

io = pruio_new(PRUIO_DEF_ACTIVE, 0, 0, 0)
IO = io.contents
if  IO.Errr: raise AssertionError("pruio_new failed (%s)" % IO.Errr)

s = datetime.datetime.now()

if pruio_config(io, NUM_SAMPLES, 0b100, 166667, 0):
    raise AssertionError("config failed (s)" % IO.Errr)

while True:
    if pruio_mm_start(io, 0, 0, 0, 0):
        raise AssertionError("mm_start failed (%s)" % IO.Errr)

    AdcV = IO.Adc.contents.Value

    #print((s - datetime.datetime.now()).microseconds)

    for i in range(NUM_SAMPLES):
        CHANNEL_1[i] = AdcV[i]

    CHANNEL_1_FFT = fft(CHANNEL_1)/NUM_SAMPLES

    CHANNEL_1_FFT[0] = 0

    CHANNEL_1_FREQS = fftfreq(len(CHANNEL_1_FFT), d=166667/1000000000.0)

    #for i in range(NUM_SAMPLES):
    #    print(CHANNEL_1[i])

    idx_1 = np.argmax(np.abs(CHANNEL_1_FFT))

    freq_1 = CHANNEL_1_FREQS[idx_1]
    freq_1 = abs(freq_1)

    print(freq_1)

pruio_destroy(io)
