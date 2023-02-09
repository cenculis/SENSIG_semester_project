import numpy as np
import scipy
import matplotlib.pyplot as plt

def plotData(data):
    k = 0
    row = int(np.shape(data)[1]/2)
    column = int(np.shape(data)[1]/row)
    plt.figure(0)
    for i in range(column):
        for j in range(row):
            plt.subplot2grid((column, row), (i, j))
            if i==0:
                plt.title("Good glass data")
            else:
                plt.title("Bad glass data")
            plt.plot(data[:, k])
            k = k+1
    plt.show()

data= np.load('combinedArray.npy')

y,x = np.shape(data)
Fs=44100

def CalcSpectrum(timedat,Fs):
    """
    Plots a Single-Sided Amplitude Spectrum of y(t)
    """
    n, sa = timedat.shape # length of the signal

    for i in range (0, sa):
        Y = scipy.fft.fft(timedat[:,i])/n # fft computing and normalization
        Y = Y[range(int(n/2))]
        if i==0:
            returndata = np.reshape(Y,(Y.shape[0],1))
        else:
            Y = np.reshape(Y,(Y.shape[0],1))
            returndata=np.concatenate((returndata, Y), axis=1)

    return returndata

plotData(data)
freqdata= CalcSpectrum(data,Fs)
np.save('combined_freq_K.npy',abs(freqdata))
plotData(abs(freqdata))



