# Main commands
## docker container list
docker ps -a

## remove docker container
docker rm <container name>

## Command to search a image from docker hub (the docker repository)
docker search <image name>

## docker image list
docker images

## remove docker image
docker rmi <image name>

## build a docker image from a Dockerfile
docker build -f <Dockerfile name> <./path>

## execute a docker image: -p = port; --rm remove after stop; -d run in background; --name container name; -it run interactive;
docker run -p <local_port:tcp_port> --rm -d --name <container name> <image name>