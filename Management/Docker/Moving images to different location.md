tutorial followed - [link](https://www.digitalocean.com/community/questions/how-to-move-the-default-var-lib-docker-to-another-directory-for-docker-on-linux)

```
sudo systemctl stop docker
sudo systemctl status docker
ps faux | grep -i docker
mkdir /home/ramu/docker
rsync -avxP /var/lib/docker/ /home/ramu/docker
sudo vim /lib/systemd/system/docker.service
# ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
# to 
# ExecStart=/usr/bin/dockerd --data-root /home/ramu/docker -H fd:// --containerd=/run/containerd/containerd.sock
sudo systemctl daemon-reload
sudo systemctl start docker
docker images
```

```
sudo systemctl stop docker
sudo systemctl status docker
ps faux | grep -i docker
sudo vim /lib/systemd/system/docker.service
ExecStart=/usr/bin/dockerd --data-root /home/ramu/docker -H fd:// --containerd=/run/containerd/containerd.sock
sudo systemctl daemon-reload
sudo systemctl start docker
docker images
```