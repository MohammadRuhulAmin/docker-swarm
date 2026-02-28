- Install swarm process

1. check docker info
```sh
docker info
```
2. docker swarm init
```sh
ip addr show eth0
docker swarm init --advertise-addr <ip_address>
docker node ls
```