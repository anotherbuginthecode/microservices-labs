# set POSTGRES_ENABLED=1 in your docker-compose.yml to tell docker that the container will use a postgres db.
# It will trigger entrypoint.sh to check if postregs connection is established before move on.
# It could be helpful if you want to use db.sqlite3 in a bootstrap build without create a docker-compose.yml with db service
# For example you could prepare a prod build with POSTGRES_ENABLED=1 and then a docker-compose.yml with db service and
# pass connection arguments to auth service
docker-build:
	docker build . -f docker/Dockerfile -t msalab01/todo:v1

# to specify a different exposed port: make run PORT=8001
docker-run:
ifdef PORT
	docker run --name lab01_todo -d -p ${PORT}:5000 msalab01/todo:v1
else
	docker run --name lab01_todo -d -p 5000:5000 msalab01/todo:v1
endif

docker-stop:
	docker rm lab01_todo -f

docker-logs:
	docker logs lab01_todo -f

docker-shell:
	docker exec -it lab01_todo bash

local-build:
	bash bootstrap.sh
local-run:
	bash start-local-server.sh
