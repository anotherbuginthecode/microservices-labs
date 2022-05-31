#!/bin/bash
IMAGE="msalab01/todo:v1"
CONTAINER="lab01_todo"
docker run -d -p 5000:5000 \
  --name=${CONTAINER} \
  -v $PWD:/app ${IMAGE}
