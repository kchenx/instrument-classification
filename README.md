instrument-classify
===================

A project to classify instruments by sound using Fourier analysis and ML algorithms

### Usage

Place all audio files in the appropriate folder in `sounds/`. Then, run `main.py`. The Fourier transform plots will be output in the appropriate folders in `images/`, and data in `fft-data`.

### Source files

| File              | Description                 |
| ----------------- | --------------------------- |
| main.py           | Main program                |
| fft.py            | Compute FFT of audio file   |
| to-wav.py         | Convert audio files to WAV  |
