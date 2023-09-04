FROM python:3.11 
# starts with python3.11 as a basline
COPY . .          
#copies all files  
RUN pip3 install -r requirements.txt 
#installs all libraries in the requirements file when the image is built
EXPOSE 5000
#runs on port 5000
ENTRYPOINT python3 app.py
#runs the file app.py when the image is run



##multi stage build

FROM no:10-alpine as build
...
...
...

FROM nginx:latest
WORKDIR /app 
#puts files into this directory
COPY --from=build_name . . 
# copies all files from the build image