#!/bin/bash
# Bash script that runs the jupyter notebook command 
#
echo "starting notebook. . ." 

jupyter trust GTZAN-Deep-Learning.ipynb
jupyter notebook --allow-root --ip 0.0.0.0 --no-browser &
sleep 1
jupyter server list
sleep infinity
