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
3. [Chatgpt help link](https://chatgpt.com/c/69a25f86-aea0-8320-b6ac-80695a6f5b58)

4. create service

```sh
docker service create alpine ping 8.8.8.8
docker service ps <service_id>
docker service logs <service_id>
docker service scale <service_name>=3
# more example:
docker service create --name web --replicas 3 nginx
```

5. To Update replicas of a service:
```sh
docker service update <service_id>  --replicas 3
```
6. Remove docker service:
```sh
docker service rm <service_id>
```