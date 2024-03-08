#!/bin/bash
#
# Spin up a docker container with the correct params

docker run --name dev -it -p 8888:8888 pabs159/music-genre-classifer:dev
