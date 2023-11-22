# Multistage Dockerfile to build and run a sample java application

This repository contains the multistage Dockerfile to build and run a sample java application..

## Requirements

To install and run this example you need:
- docker client


## Installation

The commands below set everything up to run the examples:
```
$ git clone https://github.com/nsayed123/quince-assignment.git
$ cd quince-assignment/docker/gs-rest-service
```


## Run

Make sure you are in the right directory "quince-assignment/docker/gs-rest-service"
```
docker  buildx build --platform=linux/arm64  -t myorg/myapp  . --load
docker run -p 9000:8080 -t myorg/myapp   
```

## NOTE:
1. Before running the build command please make sure you use the right --platform option.
2. If you are building the multiple architecture platform then use below command but for that you new to login in to your OCI image registry.
```
docker  buildx build --platform=linux/amd64,linux/arm64  -t <registry_name>/myapp  . --push
```

## Test
Run
```
http://localhost:9000/greeting
response - {"id":1,"content":"Hello, World!"}

http://localhost:9000/greeting?name=<your_name>
response - {"id":1,"content":"Hello, <your_name>!"}
```
