
# viewing
view all:
- docker network ls
specific details:
- docker network inspect network_namedocker

# creating
- docker network create -d bridge network_name

adds new build to network
- docker run -d --name nginx --network test nginx:alpine

