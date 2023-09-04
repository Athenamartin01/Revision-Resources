grant containers access to files outside their file system

bind mounts:

- used to attach configuration files - config file may contain sensitive info
- allows flexability and reusablility of images
- allows container config to be updated after launch

to mount files: docker run ... --mount type=bind,source=PATH, target=container_PATH

- example: docker run -d -p 80:80 --name nginx --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf nginx:alpine


volumes:

- used to share between contaniers or store data outside of a container
- managed by docker
- can use drivers to store remotely - cloud storage

docker volume create demo

docker run ... -v volume_name:container_PATH

 - example: docker run -d -it --name mysql --volume demo:/var/lib/mysql --env MYSQL_DATABASE=demo --env MYSQL_ROOT_PASSWORD=password123 mysql:5.7

docker volume rm demo