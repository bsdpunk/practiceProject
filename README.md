docker run --privileged --mount type=bind,source="$(pwd)"/target,target=/app -it vol
<br />
docker run --privileged --mount type=bind,source=/Users/dusty/docker/built/pythonContainer/app,target=/app -it api
docker run --privileged --mount type=bind,source=/Users/dusty/docker/built/pythonContainer/app,target=/app -it client

