#!/usr/bin/python3

import librosa
import numpy as np
import os
from CsvWriter import CsvWriter
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


THIRTY_SEC = 30
class AudioFeatures():

    def __init__(self, rootdir, output_filename, duration=30):
        # rootdir is the type of 
        self.csv_file = os.path.join(rootdir, output_filename)
        self.writer = CsvWriter(self.csv_file)
        self.writer.write_header()
        self.rootdir = rootdir
        self.duration = duration
        self.file = self.rootdir
        self.genres_types = ["blues", "classical", "country", 
            "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock" ]
        
    def getFiles(self):
        genres = os.listdir(os.path.join(self.rootdir, 'genres_original'))
        for g in genres:
            path = os.path.join(self.rootdir, 'genres_original', g)
            
            audio_files = os.listdir(path)
            print(f"processing: {path} \n")
            self.processFormat(path, audio_files, g)

    def processFormat(self, path, audio_files, label):
        for af in audio_files:
            print(f"processing {af}")
            af_path = os.path.join(path, af)
            self.getAudio(af_path, label)

    def getAudio(self, audio_file, label):
        y_full, sr = librosa.load(audio_file)
        
        if THIRTY_SEC % self.duration != 0:
            raise ValueError("Duration is not divisible into 30")
        else:
            iterations = int(THIRTY_SEC / self.duration) 
        
        thirty_second_sample = int(THIRTY_SEC * sr)
        y = y_full[:thirty_second_sample]

        dur_sample = int(self.duration * sr)
        for i in range(iterations):
            y_sub = y[(i * dur_sample):(dur_sample * (i + 1))]
            filename_base = os.path.basename(audio_file)
            filename, file_extension = os.path.splitext(filename_base)
            new_filename = filename + '.' + str(i) + file_extension
            print(f'Processing: {new_filename}')

            self.getFeatures(y_sub, sr, new_filename, label)
    
    # Pass in y, sr, and the label (jazz, rock, etc)
    def getFeatures(self, y, sr, filename, label):     
        # Filename
        # length
        length = librosa.get_duration(y=y, sr=sr) * sr
        # Extract features
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_stft_mean = float(np.mean(chroma_stft))
        chroma_stft_var = float(np.var(chroma_stft))

        rms = librosa.feature.rms(y=y)
        rms_mean = float(np.mean(rms))
        rms_var = float(np.var(rms))

        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        spectral_centroid_mean = float(np.mean(spectral_centroid))
        spectral_centroid_var = float(np.var(spectral_centroid))

        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        spectral_bandwidth_mean = float(np.mean(spectral_bandwidth))
        spectral_bandwidth_var = float(np.var(spectral_bandwidth))

        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        rolloff_mean = float(np.mean(rolloff))
        rolloff_var = float(np.var(rolloff))
        
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y=y)
        zero_crossing_rate_mean = float(np.mean(zero_crossing_rate))
        zero_crossing_rate_var = float(np.var(zero_crossing_rate))
        
        harmony = librosa.effects.harmonic(y)
        harmony_mean = float(np.mean(harmony))
        harmony_var = float(np.var(harmony))
        
        # Extract perceptual features
        # Compute STFT magnitude
        D = np.abs(librosa.stft(y))
        perceptr_mean = float(np.mean(librosa.perceptual_weighting(D**2, frequencies=librosa.fft_frequencies(sr=sr))))
        perceptr_var = float(np.var(librosa.perceptual_weighting(D**2, frequencies=librosa.fft_frequencies(sr=sr))))

        tempo = librosa.feature.tempo(y=y, sr=sr)

        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
        # Arrays 
        mfccs_means = np.mean(mfccs, axis=1)
        mfccs_vars = np.var(mfccs, axis=1)
        array_to_write = [filename, length, chroma_stft_mean, chroma_stft_var, rms_mean, rms_var,
                       spectral_centroid_mean, spectral_centroid_var, spectral_bandwidth_mean,
                       spectral_bandwidth_var, rolloff_mean, rolloff_var, zero_crossing_rate_mean,
                       zero_crossing_rate_var, harmony_mean, harmony_var, perceptr_mean, perceptr_var,
                       tempo]
        array_to_write.extend(mfccs_vars)
        array_to_write.extend(mfccs_means)
        array_to_write.append(label)
        print(array_to_write)
        self.writer.write_to_csv(array_to_write)


if __name__ == '__main__':
    rd = os.getcwd() + "/audio_conversions/flac"
    af = AudioFeatures(rd, "features_30_sec.csv")
    af.getFiles()

# End
