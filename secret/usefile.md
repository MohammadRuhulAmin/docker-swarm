docker secret create psql_user psql_user.txt

check secret:
```sh
docker secret ls
docker secret inspect psql_user
```
```sh
echo "myuser" | docker secret create psql_user -
echo "mypassword" | docker secret create psql_pass -

docker service create \
--name psql \
--secret psql_user \
--secret psql_pass \
-e POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass \
-e POSTGRES_USER_FILE=/run/secrets/psql_user \
postgres
```