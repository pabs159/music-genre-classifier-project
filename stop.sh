#!/bin/bash
#
# Stop the running container 

CWD=$(pwd)
echo $CWD
DC=$1
IS_RUNNING="$(docker ps -aq -f status=running -f name=$DC)"
if [ $IS_RUNNING ]; then
    echo "stopping $1"
    docker cp ${DC}:/home/music-genre-classifer/GTZAN-Deep-Learning.ipynb ${CWD}/container_notebook.ipynb
    docker stop $DC
    exit
fi
echo "nothing to stop"
