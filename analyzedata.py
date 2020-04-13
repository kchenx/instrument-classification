import csv
import numpy as np
import os
import pandas as pd

# Takes in a list of list of normalized peak amplitudes collected per trial
# and performs statistical calculations, output raw data to `dst`,
# and summary statistics to `SUMMARY.csv`
def analyze_peaks(peaks, dst, instrument):
    df = pd.DataFrame(peaks)

    # write raw data
    file_exists = os.path.isfile(dst)
    with open(dst, 'a') as f:
        headers = ['1st harmonic', '2nd harmonic', '3rd harmonic', '4th harmonic', '5th harmonic']
        writer = csv.DictWriter(f, fieldnames=headers)

        if not file_exists:
            writer.writeheader()

        df.to_csv(f, header=False, index=False)

    # write summary statistics
    with open('SUMMARY.csv', 'a') as f:
        writer = csv.writer(f)
        means = [instrument + ' means']
        means.extend(df.mean().values)
        stds = [instrument + ' stdevs']
        stds.extend(df.std().values)
        writer.writerow(means)
        writer.writerow(stds)


# Takes in the output of `compute_all_ffts` and analyzes peaks
# Input is a dictionary, with keys being instruments and values
# being a 2D list of normalized peak amplitudes collected per trial
def analyze_all_peaks(data):
    for instrument in data:
        print(instrument)
        dst = 'raw-data/' + instrument + '.csv'
        analyze_peaks(data[instrument], dst, instrument)
