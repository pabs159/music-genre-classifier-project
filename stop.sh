#!/bin/bash
#
# Stop the running container 

CWD=$(pwd)
echo $CWD
DC=$1
IS_RUNNING="$(docker ps -aq -f status=running -f name=$DC)"
if [ $IS_RUNNING ]; then
    echo "stopping $1"
    docker cp ${DC}:/home/music-genre-classifer/GTZAN-Wav.ipynb ${CWD}/GTZAN-Wav.ipynb
    docker cp ${DC}:/home/music-genre-classifer/GTZAN-Flac.ipynb ${CWD}/GTZAN-Flac.ipynb
    docker cp ${DC}:/home/music-genre-classifer/GTZAN-Mp3.ipynb ${CWD}/GTZAN-Mp3.ipynb
    docker cp ${DC}:/home/music-genre-classifer/GTZAN-Aac.ipynb ${CWD}/GTZAN-Aac.ipynb
    docker stop $DC
    exit
fi
echo "nothing to stop"
