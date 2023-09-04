# Container images

- Defines intial configurations
- file / non-sensitive env vars / ports / entrypoint

# layers:
- Images each build step adds a new layer
- aids reusability

# tags
registry_host/library_name/repo_name:version

- docker tag nginx:alpine athenamartin011/simple-demo:v1
re-tags an image

# viewing

- docker images

# manipulating images

- docker rmi Image_ID
deletes image

- docker rmi $(docker images -q)
deletes all images

- docker pull docker.io/library/nginx:alpine
pulls an image.

- docker push athenamartin011/demo_nginx:v1
pushes an image.

- docker search jenkins
searches for images on docker hub

# creating images

Docker files:
- set of instructions for building an image
- common step:
    - FROM : specififes base image
    - COPY/ADD : add files to image
    - RUN : runs generic shell command
    - EXPOSE : documents which container ports used
    - ENV : sets a env var
    - ENTRYPOINT : defines process to run on container launch
-   Dockerfile lives in the root of the github repo

check dockerfile for an example

- docker build -t athenamartin011/image_demo:v1 . 
build the image from the dockerfile in the current repo



# ignoring files

- checkout .dockerignore
this file picks files to not include into the DockerImage build

