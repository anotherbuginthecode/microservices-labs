# set POSTGRES_ENABLED=1 in your docker-compose.yml to tell docker that the container will use a postgres db.
# It will trigger entrypoint.sh to check if postregs connection is established before move on.
# It could be helpful if you want to use db.sqlite3 in a bootstrap build without create a docker-compose.yml with db service
# For example you could prepare a prod build with POSTGRES_ENABLED=1 and then a docker-compose.yml with db service and
# pass connection arguments to auth service
docker-build:
	docker build . -f docker/Dockerfile -t msalab01/auth:v1

# to specify a different exposed port: make run PORT=8001
docker-run:
ifdef PORT
	docker run --name lab01_auth -d -p ${PORT}:8000 msalab01/auth:v1
else
	docker run --name lab01_auth -d -p 8000:8000 msalab01/auth:v1
endif

docker-stop:
	docker rm lab01_auth -f

docker-logs:
	docker logs lab01_auth -f

docker-shell:
	docker exec -it lab01_auth bash

local-build:
	bash bootstrap.sh
local-run:
	bash start_local_server.sh
