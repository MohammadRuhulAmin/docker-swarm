
init:
```sh
docker swarm init
docker stack deploy -c docker-compose.yml fastapi_stack
```
down service:
```sh
docker stack ls
docker stack services fastapi_stack
```
docker service down:
```sh
docker stack rm fastapi_stack
```