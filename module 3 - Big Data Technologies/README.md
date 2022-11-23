# Annotations 📜✍️

## Chapter 1 - Microservices Architecture: Docker

### 1.1. Monoliths and Microservices Architecture

- Monolith Architecture Challenges:
1. Slow release cycle;
2. Updates are less frequent;
3. The necessity to build the whole system after every update;
4. Computing power to run the whole workload;
5. Vertical scalability;
- Microservices Architecture Advantages:
1. Fast release cycle;
2. Small and frequent updates;
3. Exclusive update for each part of the system;
4. Computing capacity that fits the needs of each part;
5. Horizontal scalability;

### 1.2. VM vs Container

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/48625700/203542477-81e79654-4f36-417c-bff5-783066f35d5b.png">
</p>

<p align="center">
  Figure 1 - Virtual Machine and Container Image comparison
</p>

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
## Chapter 2- Microservices Architecture: Kubernetes

### 2.1. Kubernetes: origin, architecture, and benefits

- Origin

Google created it to attend to the demand of managing many resources at the same time. It was hard to build and deploy a lot of resources, so, Kubernetes is the solution to manage this kind of situation.

- Architecture

The developer has to create a description of the resources that the app has (app descriptor) and then send it to the Kubernetes master. The Kubernetes master after receiving the app descriptor will make some decisions by itself to define how to create and manage these resources. So, the solution will be deployed by the Kubernetes master based on the app descriptor. Figure 2 shows that process.

<p align="center">
  <img width="750" src="https://user-images.githubusercontent.com/48625700/203544070-9f27d512-6978-439f-8fa5-a6d4a7d7d02e.png">
</p>

<p align="center">
  Figure 2 - Overview of Kubernetes process
</p>

The Kubernetes master is composed of two main structures, the Control plane (master node) and the Worker node(s). Figure 3 shows this structure.

<p align="center">
  <img width="650" src="https://user-images.githubusercontent.com/48625700/203544386-1ac07bc5-b1c0-4b6b-a74c-f8f02819785d.png">
</p>

<p align="center">
  Figure 3 - Kubernetes master strucutre
</p>

- Control Plane (master node)
    - API server: it is the channel between the users and the Kubernetes elements.
    - Controller Manager: it has the responsibility to manage the cluster.
    - Scheduler: it has to decide which work node will do a task.
    - etcd: data storage (key-value) that stores metadata about the cluster.
- Worker node(s)
    - Kubelet: it has to be installed in each work node, it does the communication between the work nodes and the control plane (master node)/API server.
    - Container Runtime: the engine to run the containers.
    - kube-proxy: it manages the network traffic in the Kubernetes cluster.
- Pods: they are each part of the application. It will be deployed in each work node.
- Benefits
1. Easy and automatic deployment;
2. Automatic environment setting;
3. Hardware used efficiently;
4. Health-checking and automatic backup;
5. Automatic scalability;
6. Makes easy the app development;

