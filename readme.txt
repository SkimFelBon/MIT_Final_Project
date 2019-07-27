# Create DockerFile
# build image
docker build .

# build image with tag name
docker build -t dude/man:v2 .
docker build -t skim/mitfp:v1 .

# Run image "ubuntu 18.04"
docker run -it d131e0fa2585

# Share folder /mnt
docker run -it -v c:/MyPythonScripts/OSSU/CS50onTwitch/dockerTutor:/mnt d131e0fa2585
docker run -it -v c:/MyPythonScripts/myGitHub/MIT_Final_Project:/mnt d1b046b09f5e
docker run -v c:/MyPythonScripts/myGitHub/MIT_Final_Project:/MIT_Final_Project -it d1b046b09f5e
# install vim, inside ubuntu
apt-get install vim

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

# Jump to container
docker exec -it webserver /bin/bash
docker exec -it mit_final_project_v1 /bin/bash

installed apache 2 and vim
cd /etc/apache2/
cat sites-enabled/000-default.conf
cd /var/www/html
service apache2 restart
