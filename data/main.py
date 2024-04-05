#!/usr/bin/python3

import argparse
import os
from CsvWriter import CsvWriter
from AudioFeatures import AudioFeatures

if __name__ == '__main__':
    # Create argument parser
    parser = argparse.ArgumentParser(description='Process audio files to extract features.')

    # Add arguments
    parser.add_argument('-d', '--rootdir', required=True, type=str, help='Root directory containing audio files.')
    parser.add_argument('-o', '--output_filename', required=True, type=str, help='Output filename for CSV.')
    parser.add_argument('-n', '--number_samples', required=False, type=int, default=30, help='Number of samples [Default is 1 per song].')

    # Parse arguments
    args = parser.parse_args()

    # Check if rootdir and output_filename are provided
    if args.rootdir is None or args.output_filename is None:
        parser.error('Please provide both --rootdir and --output_filename arguments.')
    
    # Initialize AudioFeatures instance
    af = AudioFeatures(args.rootdir, args.output_filename, args.number_samples)

    # Process audio files
    af.getFiles()

