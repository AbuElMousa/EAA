import numpy as np
import bisect
from numpy.fft import fft
import matplotlib.pyplot as plt
from scipy.signal import correlate, hilbert
import time

def fff

'''
find direction
cross correlate
distance
toasamplesmatrix
'''

def computeTOASamplesMatrix(self):
    arrayTOA = []
    for i in range(self.nmics):
        temparray = []
        for j in range(self.nmics):
            temparray.append(self.distance(self.micpos[i], self.micpos[j]) /
                             (self.c * (1 / (self.nsamples / (self.endtime - self.timestart)))))


def build_TOA_matrix(mic_data):
    """Builds the Time of Arrival matrix for the given input

    Write a mathematical explanation?

    :param mic_data: a list of dictionaries with input information for the current iteration
    """
    TOA = []
    for current_mic in mics:
        current_mic_toa = []
        for alt_mic in mics:
            mic_to_mic_dist = distance.euclidian(current_mic['position'], alt_mic['position'])
            
            current_mic_toa.append(mic_to_mic_dist)

from scipy.spatial import distance
# 
#distance.euclidian(a, b), where a and b are tuples


def distance(pos_1: tuple, pos_2: tuple):
    """Calculates the distance between two microphone positions

    """
    # pos1 and pos2 need to be provided as [x1, y1] and [x2, y2]
    dist = np.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2)
    # print(dist)
    return dist

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
===============================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class OAS:
    def __init__(self, nmics, sourcepos, frequencies): 
                 noiselevel='low'):
        self.nmics = nmics
        self.micpos = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        self.sourcepos = sourcepos
        self.nsamples = # length of the inputs
        self.frequencies = frequencies
        self.c = 330
        self.timestart = 0
        self.endtime = #determine
        self.TOA_samples = self.computeTOASamplesMatrix()


    def runxcorr(self, debug = 0):
        ofile = open('activesource.txt', 'w')
        # Run a cross correlation, in time, across all available channels.
        # Returns the cross correlation value of the combinations.
        matlist = []
        matlist1 = []
        for i in range(self.nmics):
            templist = []
            templist1 = []
            for j in range(self.nmics):
                # np.convolve(x, np.ones((N,)) / N, mode='valid')
                # Re-adjust the output signal to a rolling mean
                meanint = 10
                xconvolve1 = np.convolve(self.nChSignals[i], np.ones((meanint,))/meanint, mode='valid')
                xconvolve2 = np.convolve(self.nChSignals[j], np.ones((meanint,))/meanint, mode='valid')

                #plt.plot(xconvolve1)
                #plt.plot(xconvolve2)
                #plt.show()

                # xcorrelate = correlate(self.nChSignals[i], self.nChSignals[j], mode='full', method='fft')
                xcorrelate = correlate(xconvolve1, xconvolve2, mode='full')
                xcorrelatefft = fft(xcorrelate)
                xcorrenvelope = np.abs(hilbert(xcorrelate))
                plt.plot(xcorrenvelope)
                #plt.show()
                xcorrmaxpos = np.argmax(xcorrenvelope)
                # print(xcorrmaxpos)

                tcorrelate = np.linspace(0, len(xcorrelate) - 1, num=len(xcorrelate))
                tcorr_center = len(tcorrelate) / 2

                # fft_max_period = len(y_corr_fft)/np.argmax(abs(y_corr_fft[0:len(y_corr_fft)/2]))
                # corr_index_low[k] = int(corr_index_max  - 1.5*fft_max_period), same for highind just change - to +
                # if corr_index_high[k] > len(ycorr_envelope) -1 :  corr_index_high[k] =  len(ycorr_envelope)- 1

                # fftmaxp = len(xcorrelatefft)/np.argmax(np.abs(xcorrelatefft[0:len(xcorrelatefft)//2]))
                # lowcorrind = int(xcorrmaxpos - 1.5*fftmaxp)
                # if lowcorrind < 0: lowcorrind = 0
                # highcorrind = int(xcorrmaxpos + 1.5*fftmaxp)
                # if highcorrind > len(xcorrenvelope)-1: highcorrind = len(xcorrenvelope)-1

                # xcorr = xcorr - ones(len(xcorr)) * xcorr_center
                tcorrelate = tcorrelate - np.ones(len(tcorrelate)) * tcorr_center


                p = bisect.bisect(tcorrelate, self.TOA_samples.item((i,j)))
                templist1.append(p)

                # if corr_index_low[k] <= p and p <= corr_index_high[
                #     k]:  # only search if it's within range of the central maximum
                #     for i in arange(p, corr_index_high[k], 1):  # search upward from p to len(xo)
                #         if fabs(xcorr[i] - del_TOA_mic_pairs[k, n, m]) <= box_samples:

                if debug:
                    plt.plot(xcorrenvelope)
                    plt.show()
                templist.append(xcorrmaxpos)
            matlist.append(templist)
            matlist1.append(templist1)
        xcorrmaxmat = np.matrix(matlist)
        tcorrmat = np.matrix(matlist1)
        print(self.TOA_samples)
        print(xcorrmaxmat)
        print(tcorrmat)
        subs = np.subtract(xcorrmaxmat, tcorrmat)
        minrow = subs.min(0)
        subs = np.subtract(subs.min(0), minrow.min())
        subs = np.divide(subs, (self.nsamples / (self.endtime - self.timestart)))
        # THIS VALUE OF SUBS IS WHAT WE NEED TO COMPUTE THE DIRECTION!!
        print('delays: {}\n'.format(subs))
        # print('delays: {}'.format(subs))
        self.computeDirection(subs)
        return xcorrmaxmat

    def computeDirection(self, rMinTimeRow):

        dpos = []

        minpos = np.argmin(rMinTimeRow)
        # print('\nminpos\n', minpos)

        # This is based off of the quadrants, make the mics match the quadrants. mic1, q1, mic2, q4, mic3, q2, mic4, q3
        if minpos > 2:
            const = 180
        else:
            const = 0

        ipos = self.micpos[minpos]
        miclist = [0, 1, 2, 3]
        miclist.remove(minpos)
        for i in miclist:
            dpos.append(np.subtract(self.micpos[i], ipos))

        dposmat = np.matrix([dpos[0], dpos[1], dpos[2]])
        # opfile.write('dposmat: {}\n'.format(dposmat))
        print('\ndposmat\n', dposmat)

        pseudoinv = np.linalg.pinv(dposmat)
        print('\npseudoinv\n', pseudoinv)

        cdTmat = np.delete(rMinTimeRow, minpos)
        cdTmat = np.multiply(cdTmat, self.c)
        cdTmat = np.transpose(cdTmat)
        print(cdTmat)

        uv = np.dot(pseudoinv, cdTmat)
        print('\nuv\n', uv)

        theta = np.rad2deg(np.arctan2(uv[1], uv[0]))
        if theta < 0:
            theta = theta + 180
        elif theta >=0:
            theta = theta - 180

        actual = np.rad2deg(np.arctan2(self.sourcepos[1], self.sourcepos[0]))

        print('{},{},{},{},snr0,{}'.format(self.sourcepos[0], self.sourcepos[1], theta.min(), actual, self.nChSnr[0]))

    def computeTOASamplesMatrix(self):
        arrayTOA = []
        for i in range(self.nmics):
            temparray = []
            for j in range(self.nmics):
                temparray.append(self.distance(self.micpos[i], self.micpos[j]) /
                                 (self.c * (1 / (self.nsamples / (self.endtime - self.timestart)))))
            arrayTOA.append(temparray)
        # print(arrayTOA)
        return np.matrix(arrayTOA)

    def distance(self, pos1, pos2):
        # pos1 and pos2 need to be provided as [x1, y1] and [x2, y2]
        dist = np.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2)
        # print(dist)
        return dist


OAS = OAS(4, [-8, -17], [5, 10, 15, 20])
OAS.runxcorr()
