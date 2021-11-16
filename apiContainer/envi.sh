function runapi {
docker run --privileged --mount type=bind,source=/Users/dusty/docker/built/app,target=/app -it api
}
