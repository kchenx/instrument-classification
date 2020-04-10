from matplotlib import pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.io import wavfile as wav
from scipy import optimize
import os

# Plot and save the Fourier transform of wav file at `path` to `dst`
def compute_fft(path, imgdst, datadst = None):
    # data processing and fft calculations
    rate, data = wav.read(path)
    try:
        data = data[:, 0]
    except IndexError:
        pass
    samples = data.shape[0]
    datafft = fft(data)
    fftabs = abs(datafft)
    # TO DO: normalization of fft values
    # TO DO: scaling + shifting of freq values
    freqs = fftfreq(samples, 1/rate)
    np.savetxt(datadst,
               np.c_[freqs[:int(freqs.size/2):1000], fftabs[:int(freqs.size/2):1000]],
               delimiter=",")

    # creating image
    plt.figure()
    plt.xlim([10, rate/2])
    plt.xscale("log")
    plt.grid(True)
    plt.xlabel("Frequency (Hz)")
    plt.title(path)
    plt.plot(freqs[:int(freqs.size/2)], fftabs[:int(freqs.size/2)])
    plt.savefig(imgdst)

    # instrument average calculations
    fftabs = fftabs[:int(freqs.size / 2)]
    freqs = freqs[:int(freqs.size / 2)]
    lfreq = 20  # freq bounds
    ufreq = 20000
    ind = np.where(np.logical_and(freqs >= lfreq, freqs <= ufreq))
    return freqs[ind], fftabs[ind]

def compute_all_ffts():
    piano = []   # initializing instrument average storage TO DO: implement for other instruments
    for root, dirs, files in os.walk("sounds"):
        for file in files:
            path = os.path.join(root, file)
            (pre, ext) = os.path.splitext(path)
            if ext in [".wav"]:
                body = os.path.sep.join(pre.split(os.path.sep)[1:])
                imgdst = os.path.join("images", body + ".png")
                datadst = os.path.join("fft-data", body + ".csv")
                freq, fft = compute_fft(path, imgdst, datadst)

                # instrument average calculations
                if 'piano' in path:
                    # TO DO: convert freq, fft (discrete data) to smooth function and append to piano array

                # elif 'xylophone' in path:
    # avgpiano = np.average(piano, axis=0)
    pass





