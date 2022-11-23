# Annotations 📜✍️

## Chapter 1 - Microservices Architecture: Docker

### 1.1. Monoliths and Microservices Architecture

- Monolith Architecture
    - Challenges:
1. Slow release cycle;
2. Updates are less frequent;
3. The necessity to build the whole system after every update;
4. Computing power to run the whole workload;
5. Vertical scalability;
- Microservices Architecture
    - Advantages:
1. Fast release cycle;
2. Small and frequent updates;
3. Exclusive update for each part of the system;
4. Computing capacity that fits the needs of each part;
5. Horizontal scalability;

### 1.2. VM vs Container

![image](https://user-images.githubusercontent.com/48625700/203542477-81e79654-4f36-417c-bff5-783066f35d5b.png)

### 1.3. Docker: basic commands

```
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

## execute a docker image
### params: -p = port; --rm remove after stop; -d run in background; --name container name; -it run interactive;
docker run -p <local_port:tcp_port> --rm -d --name <container name> <image name>
```
