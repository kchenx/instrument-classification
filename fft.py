from matplotlib import pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.io import wavfile as wav
import os

# Plot and save the Fourier transform of wav file at `path` to `dst`
def compute_fft(path, imgdst, datadst = None):
    rate, data = wav.read(path)
    try:
        data = data[:,0]
    except IndexError:
        pass
    samples = data.shape[0]
    datafft = fft(data)
    fftabs = abs(datafft)
    freqs = fftfreq(samples, 1/rate)

    np.savetxt(datadst,
               np.c_[freqs[:int(freqs.size/2):1000], fftabs[:int(freqs.size/2):1000]],
               delimiter=",")

    plt.figure()
    plt.xlim([10, rate/2])
    plt.xscale("log")
    plt.grid(True)
    plt.xlabel("Frequency (Hz)")
    plt.title(path)
    plt.plot(freqs[:int(freqs.size/2)], fftabs[:int(freqs.size/2)])
    plt.savefig(imgdst)

def compute_all_ffts():
    for root, dirs, files in os.walk("sounds"):
        for file in files:
            path = os.path.join(root, file)
            (pre, ext) = os.path.splitext(path)
            if ext in [".wav"]:
                body = os.path.sep.join(pre.split(os.path.sep)[1:])
                imgdst = os.path.join("images", body + ".png")
                datadst = os.path.join("fft-data", body + ".csv")
                compute_fft(path, imgdst, datadst)
