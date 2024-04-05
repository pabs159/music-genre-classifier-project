#!/usr/bin/python3

import csv

class CsvWriter:
    def __init__(self, filename):
        self.filename = filename
        self.header = ["filename", "length", "chroma_stft_mean", "chroma_stft_var", "rms_mean", "rms_var",
            "spectral_centroid_mean", "spectral_centroid_var", "spectral_bandwidth_mean", "spectral_bandwidth_var",
            "rolloff_mean", "rolloff_var", "zero_crossing_rate_mean", "zero_crossing_rate_var", "harmony_mean",
            "harmony_var", "perceptr_mean", "perceptr_var", "tempo",
            "mfcc1_mean", "mfcc1_var", "mfcc2_mean", "mfcc2_var", "mfcc3_mean", "mfcc3_var", "mfcc4_mean", "mfcc4_var",
            "mfcc5_mean", "mfcc5_var", "mfcc6_mean", "mfcc6_var", "mfcc7_mean", "mfcc7_var", "mfcc8_mean", "mfcc8_var",
            "mfcc9_mean", "mfcc9_var", "mfcc10_mean", "mfcc10_var", "mfcc11_mean", "mfcc11_var", "mfcc12_mean", "mfcc12_var",
            "mfcc13_mean", "mfcc13_var", "mfcc14_mean", "mfcc14_var", "mfcc15_mean", "mfcc15_var", "mfcc16_mean", "mfcc16_var",
            "mfcc17_mean", "mfcc17_var", "mfcc18_mean", "mfcc18_var", "mfcc19_mean", "mfcc19_var", "mfcc20_mean", "mfcc20_var",
            "label"]

    def write_header(self):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.header)
    
    def write_to_csv(self, data):
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)




if __name__ == '__main__':
    # Specify the filename for the CSV file
    csv_filename = "output.csv"

    # Create an instance of StringArrayCSVWriter
    csv_writer = CsvWriter(csv_filename)

    # Call the write_to_csv method to generate the CSV file
    csv_writer.write_header()
    csv_writer.write_to_csv(["test", "testing"])

    print("CSV file has been created successfully.")

