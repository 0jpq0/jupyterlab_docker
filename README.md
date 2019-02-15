# jupyterlab-docker

Jupyterlab Docker image

This image is configured as an automated build on Docker Hub: <https://hub.docker.com/r/0jpq0/jupyterlab/>.

You can pull the lastest automated build using the docker pull command: `docker pull 0jpq0/jupyterlab` or clone this repository and build the image locally using `docker-compose build`.

```bash
sudo docker run -p 8888:8888 -v /data/notes:/opt/app/data -e password="password" -it 0jpq0/jupyterlab
```

