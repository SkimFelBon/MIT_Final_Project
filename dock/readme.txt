# Create DockerFile
# build image
docker build .

# to create image
docker build --tag=image_name .

# build image with tag name
docker build -t dude/man:v2 .
docker build -t skim/mitfp:v1 .

# to rename container (not image)
docker rename [container name] cs50 (e.g. docker rename 7dbd85cec821 cs50)

# to restart container
docker restart [ContainerID]

# to start container run
docker start -a [ContainerID]

# Jump to container
docker exec -it webserver /bin/bash
docker exec -it mit_final_project_v1 /bin/bash

# Run image "ubuntu 18.04"
docker run -it d131e0fa2585

# Share folder and delete container after exit
docker run -it --name my-linux-container --rm -v C:\MyPythonScripts\myGitHub\MIT_Final_Project:/my_data ubuntu bash

# Share folder /mnt
docker run -it -v c:/MyPythonScripts/OSSU/CS50onTwitch/dockerTutor:/mnt d131e0fa2585
docker run -it -v c:/MyPythonScripts/myGitHub/MIT_Final_Project:/mnt d1b046b09f5e
docker run -v c:/MyPythonScripts/myGitHub/MIT_Final_Project:/MIT_Final_Project -it d1b046b09f5e
# install vim, inside ubuntu
apt-get install vim

# latest build order
docker build --tag=project_heroku .

# Run update to get a cash of local storages  (apt is a package manager)
apt-get update

# install pip

# install python3

# install flask

# this one worked docker run -td --name mycontainer -p 80:80 demoubuntu2


#-------------------
useful commands:
# To create container
docker run -td --name webserver -p 80:80 ubuntu
docker run -td --name mit_final_project_v1 -p 80:80 skim/mitfp:v1

# To remove container
docker container rm webserver

# Show running containers
docker ps

# to run ide50 container
docker run --privileged -e "IP=127.0.0.1" -e "PORT=8080" --name ide50 -d -p 5050:5050 -p 8080-8082:8080-8082 cs50/ide

installed apache 2 and vim
cd /etc/apache2/
cat sites-enabled/000-default.conf
cd /var/www/html
service apache2 restart
