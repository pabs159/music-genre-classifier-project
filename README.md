# Music Genre Classifier Project

Project for ECE 381V

## Docker 
To pull the container:
```
docker pull pabs159/music-genre-classifer:<tag>
```

Optinally to build and run:

```
docker build . -t pabs159/music-genre-classifer:<tag> -f docker/Dockerfile
docker run -it -p 8888:8888 pabs159/music-genre-classifer:<tag>
```

You can run container based on name after its been built or pulled via its tag
You can also stop it via the stop script

``` 
./run.sh <container> 
./stop.sh <container>
```

If the container is already running then it will notify the user. 
When running the _stop.sh_ command it will copy the 4 notebooks out 
of the container and into the root of the project.

```
pabs:music-genre-classifier-project$ ./stop.sh dev
/home/pabs/GitRepos/UT_Grad_School/music-genre-classifier-project
stopping dev
Successfully copied 3.27MB to /home/pabs/GitRepos/UT_Grad_School/music-genre-classifier-project/GTZAN-Wav.ipynb
Successfully copied 3.27MB to /home/pabs/GitRepos/UT_Grad_School/music-genre-classifier-project/GTZAN-Flac.ipynb
Successfully copied 3.27MB to /home/pabs/GitRepos/UT_Grad_School/music-genre-classifier-project/GTZAN-Mp3.ipynb
Successfully copied 3.27MB to /home/pabs/GitRepos/UT_Grad_School/music-genre-classifier-project/GTZAN-Aac.ipynb
```

This container was built on top of a tensorflow 2.11 container with some additional packages. This container is stored in [docker hub](https://hub.docker.com/layers/pabs159/music-genre-classifer/dev/images/sha256-141420b5f2c40583fd5e9d7a49fba537d87fa4787a6f336e0085191e31dd1235?context=explore)

## Data utilities

#### Convert.sh 
- Takes in a:
  - Input directory
  - Output directory 
  - Format to convert 
- Example usage:
  - `./convert.sh  --input genres_original/ --output audio_conversions/ --format flac`
- Upon execution this script will duplicate the original directory structure of the input with the audio file types changed. 
- For instance after converting the original GTZAN dataset to flac, it will be structued as below: 

```
audio_conversions/flac/
├── features_30_sec.csv
├── features_3_sec.csv
└── genres_original
    ├── blues
    ├── classical
    ├── country
    ├── disco
    ├── hiphop
    ├── jazz
    ├── metal
    ├── pop
    ├── reggae
    └── rock
```

#### AudioFeatures.py

- Takes in a rootdirectory and the output file path
  - Also takes an optional duration argument to split the audio up 
    - Duration of 3 would split the file into 10, 3 second segments
    - **NOTE:** Must be divisble into 30
  - main.py provides a cli interface to call this script as an entrypoint  
    - ex: `/main.py -d audio_conversions/flac/ -o features_3_sec.csv -n 10`

#### CsvWriter.py
- Is called from _AudioFeatures.py_ to output the results of the feature extraction
  - It takes one argument that is the filename of where to write 
  - It then writes the header along with the data
- These CSV files match the format of the original [GTZAN dataset](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)

### Training 
- After you have converted the wav formated files of the original dataset, and produced the corresponding csv file. You can create a notebook (for install there is a notebook for each audio format) and run it. You can also make varying lengths of features for more analysis (3 sec samples vs 10 sec samples). 
