#!/usr/bin/python3

import librosa
import numpy as np
import os

class AudioFeatures():

    def __init__(self, rootdir):
        # rootdir is the type of file to be process
        self.rootdir = rootdir
        # ..../flac/genres_original/...
        self.file = self.rootdir
        
    def getFiles(self):
        genres = os.listdir(os.path.join(self.rootdir, 'genres_original'))
        for g in genres:
            path = os.path.join(self.rootdir, 'genres_original', g)
            audio_files = os.listdir(path)
            print(f"processing: {path} \n")
            self.processFormat(path, audio_files)

    def processFormat(self, path, audio_files):
        for af in audio_files:
            print(f"processing {af}")
            af_path = os.path.join(path, af)
            self.getFeatures(af_path)

    def getFeatures(self, audio_file):     
        y, sr = librosa.load(audio_file)

        duration = librosa.get_duration(y=y, sr=sr)

        # Extract features
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_stft_mean = np.mean(chroma_stft)
        chroma_stft_var = np.var(chroma_stft)

        rms = librosa.feature.rms(y=y)
        rms_mean = np.mean(rms)
        rms_var = np.var(rms)

        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        spectral_centroid_mean = np.mean(spectral_centroid)
        spectral_centroid_var = np.var(spectral_centroid)

        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        spectral_bandwidth_mean = np.mean(spectral_bandwidth)
        spectral_bandwidth_var = np.var(spectral_bandwidth)

        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
        mfccs_means = np.mean(mfccs, axis=1)
        mfccs_vars = np.var(mfccs, axis=1)




if __name__ == '__main__':
    rd = os.getcwd() + "/audio_conversions/flac"
    af = AudioFeatures(rd)
    af.getFiles()

'''

# Load audio file
audio_file = "genres_original/blues/blues.00000.flac"

mfcc16_mean = mfccs_means[15]
mfcc16_var = mfccs_vars[15]
mfcc17_mean = mfccs_means[16]
mfcc17_var = mfccs_vars[16]
mfcc18_mean = mfccs_means[17]
mfcc18_var = mfccs_vars[17]
mfcc19_mean = mfccs_means[18]
mfcc19_var = mfccs_vars[18]
mfcc20_mean = mfccs_means[19]
mfcc20_var = mfccs_vars[19]

# You can print or use these values as needed
print("Feature Name\t\t\t\tMean\t\t\t\t\tVariance")
print("-" * 80)
print(f"Chroma STFT\t\t\t\t{chroma_stft_mean}\t\t\t{chroma_stft_var}")
print(f"RMS\t\t\t\t\t\t{rms_mean}\t\t\t{rms_var}")
print(f"Spectral Centroid\t\t\t{spectral_centroid_mean}\t\t\t{spectral_centroid_var}")
print(f"Spectral Bandwidth\t\t\t{spectral_bandwidth_mean}\t\t\t{spectral_bandwidth_var}")
print("-" * 80)
print("MFCCs")
print("-" * 80)
print("MFCC\t\t\t\t\tMean\t\t\t\t\tVariance")
for i in range(15, 20):
    print(f"MFCC{i+1}\t\t\t\t\t{mfccs_means[i]}\t\t\t{mfccs_vars[i]}")
print(f"Duration: {duration}")

array_length = len(y)
print("Length of the audio array:", array_length, "samples")
'''
