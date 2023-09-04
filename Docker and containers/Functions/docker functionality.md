# container interactions

# launch container

- docker run -it --name container_name ubuntu:lastest /bin/sh -c "shell_command"

-it: launches shell session allows for interaction

--name: sets the name for the container

/bin/sh runs shell executable 
-c runs shell commands in the executable

- docker run -d -p (ip:)80:80 --env MY_VAR=Hello --name nginx nginx:alpine

-d: runs it in detached mode

-80:80 : host port : container port .  
ip address to listen on can also be added if wanting to keep it private

--env : sets environment vairable 


# view containers

- docker ps -a  

-used to view all containers 

- docker logs nginx

-view logs for a container
# Stop/Remove containers

- docker stop nginx ubuntu && docker rm nginx ubuntu

-first part stops containers, second part removes containers

- docker start nginx 

-starts an existing containers


# Useful libraries

- jenkins/jenkins:lts


# logging in to docker hub

- docker login
    - username 
    - password

- docker logout