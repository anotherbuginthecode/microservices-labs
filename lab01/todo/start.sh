#!/bin/bash
IMAGE="msalab01/todo"
CONTAINER="lab01_todo"
docker build -t ${IMAGE} .
docker run -d -p 5000:5000 \
  --name=${CONTAINER} \
  -v $PWD:/app ${IMAGE}
