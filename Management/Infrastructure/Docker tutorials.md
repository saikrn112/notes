**Docker commands compilation sheet for reference 

  

Tutorial - [Link](https://rominirani.com/docker-tutorial-series-a7e6ff90a023)

Removing stuff - [Link](https://www.tecmint.com/remove-docker-images-containers-and-volumes/)

Hub - [Link](https://hub.docker.com/)

Cheat Sheet - [Link](https://hackernoon.com/docker-commands-the-ultimate-cheat-sheet-994ac78e2888)

Changing default location - [Link](https://forums.docker.com/t/how-do-i-change-the-docker-image-installation-directory/1169/20)

Docker search <container>
Docker ps - process status 

Docker ps -a --- all the process 

Docker stop <container name> 

Docker run <container>

Docker port <container name> -- to check which port is assigned to this process by the host system 

Docker system -- to check size, clean up unused containers etc 

Docker images -- images present in the system and their size 

Docker rmi <image name> -- remove the container 

Docker stats -- real time top only for docker images 

Docker commit <container name> <user/repo> -- to commit changes to the docker before removing the container 

Docker attach <container name> -- will attach to the container 

Docker login -- will log you into the corresponding docker 

Docker push -- will push to the repo

Docker volume -- commands for data volumes 

Docker exec <container name> <commands> -- executes commands in docker terminal and result is outputted where command is executed 

Docker inspect <container name> -- will show the container info in json output

Docker build <Dockerfile path> -- builds the docker file 

Docker create <image> -- docker run - docker start 

  

docker stop $(docker ps -a -q) -- stops all containers 

docker rm $(docker ps -qa) --- removes all containers 

docker volume rm $(docker volume ls  -q --filter dangling=true) -- removes all volumes 

docker rmi $(docker images -aq) --- removes all images 

docker system prune --volumes -- remove unused space

docker rmi $(docker images -q --filter "dangling=true") -- removing dangling images  
  

  
  
  

Docker run 

-i -- interactive 

-d -- detached state

-P -- assign random port to the process in the host 

-p -- assign specified port to the process 

--rm -- automatically remove the container when exits 

-v -- data volumes 

--volumes-from <list> -- mounts volumes that are used by other containers 

-t -- assign some psuedo tty 

-it -- interactive psuedo tty 

--link -- link the containers by specifying the container name; no need to publish the port**