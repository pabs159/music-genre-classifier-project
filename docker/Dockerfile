FROM pabs159/music-genre-classifer:tensorflow-2.11 

RUN mkdir -p /home/music-genre-classifer
RUN pip install notebook
WORKDIR /home/music-genre-classifer
COPY ./docker/run-notebook.sh /usr/bin
COPY data ./data
COPY GTZAN-Deep-Learning.ipynb .
RUN chmod +x /usr/bin/run-notebook.sh

EXPOSE 8888
CMD ["run-notebook.sh"]
