#!/bin/bash
# Convert audio files using ffmpeg

# Function to display help message
display_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "Example usage: ./convert.sh  --input genres_original/ --output audio_conversions/ --format flac"
    echo "Options:"
    echo "  -a, --aformat    Specify the conversion ex: s16:441000 is 16bit at 44.1 kHz"
    echo "  -f, --format     Specify output aformat"
    echo "  -h, --help       Display this help message"
    echo "  -i, --input      Specify the input directory"
    echo "  -o, --ouput      Specify the output directory"
}

process_keyword_args() {
    while [[ "$#" -gt 0 ]]; do
        case $1 in
            -i|--input)
                INPUT_DIR="$2"
                shift
                ;;
            -o|--output)
                OUTPUT_DIR="$2"
                shift
                ;;
            -f|--format)
                CONV_FMT="$2"
                shift
                ;;
            -a|--aformat)
                CONV_FMT="$2"
                shift
                ;;
            -h|--help)
                display_help
                exit 0
                ;;
            *)
                echo "Error: Unknown option $1"
                display_help
                exit 1
                ;;
        esac
        shift
    done
}

# Process keyword arguments
process_keyword_args "$@"

PWD=$(pwd)
VALID_FORMATS=("flac" "mp3" "wav")

# Check if output format is provided
if [[ -z $CONV_FMT ]] && [[ $(echo ${VALID_FORMATS[@]} | grep -w $CONV_FMT) ]]; then
    echo "Error: Output format not specified or is not supported"
    display_help
    exit 1
fi

INPUT_DIR=$(echo "$INPUT_DIR" | sed 's:/*$::')
OUTPUT_DIR=$(echo "$OUTPUT_DIR" | sed 's:/*$::')

OUTPUT_PATH="$PWD/$OUTPUT_DIR/$CONV_FMT"

echo "Using input directory: ${INPUT_DIR}"
echo "Writing files to: ${OUTPUT_PATH}"

mkdir -p $OUTPUT_PATH

tree -dfi --noreport $INPUT_DIR | xargs -I{} mkdir -p "$OUTPUT_PATH/{}"

# To Do
#if [[ -z $AFORMAT ]]; then
#fi

for i in $INPUT_DIR/*/*.wav; do ffmpeg -hide_banner -loglevel error -i "$i" "$OUTPUT_PATH/${i%.*}.$CONV_FMT"; done

