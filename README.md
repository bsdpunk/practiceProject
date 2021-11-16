Why I didn't use pipenv:
https://drewdevault.com/2021/11/16/Python-stop-screwing-distros-over.html?fbclid=IwAR1Q9B4g7DW2xW7yTe5edwNUnaUe7K8izz9c_J74UA3hc_VnaiWITHGCZpM

docker run --privileged --mount type=bind,source="$(pwd)"/target,target=/app -it vol
<br />
docker run --privileged --mount type=bind,source=/Users/dusty/docker/built/pythonContainer/app,target=/app -it api
<br />
docker run --privileged --mount type=bind,source=/Users/dusty/docker/built/pythonContainer/app,target=/app -it client

