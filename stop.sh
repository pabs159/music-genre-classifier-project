#!/bin/bash
#
# Stop the running container 
DC=$1
IS_RUNNING="$(docker ps -aq -f status=running -f name=$DC)"
if [ $IS_RUNNING ]; then
    echo "stopping $1"
    docker stop $DC
    exit
fi
echo "nothing to stop"
