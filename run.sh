#!/bin/bash
#
# Spin up a docker container with the correct params

if [[ ( $@ == "--help") ||  $@ == "-h" || $@ == "" ]]
then 
cat <<EOF
Usage: run.sh <container name>
EOF
exit
fi

DC=$1

EXIST="$(docker ps -a -q -f name=$DC)"
IS_RUNNING="$(docker ps -aq -f status=running -f name=$DC)"
if [ $EXIST ]; then
    if [ $IS_RUNNING ]; then
        echo "container $DC is running!"
        exit
    fi
    echo "container already exist, but is not running"
    docker start -a $DC
    exit
fi
echo "running container..."
docker run --name $DC -it -p 8888:8888 pabs159/music-genre-classifer:${DC}
