docker-build:
	docker build . -t msalab01/webapp:v1 -f docker/Dockerfile
docker-run:
	docker run -it -d -p 80:80 --rm --name lab01_webapp msalab01/webapp:v1
docker-stop:
	docker container rm lab01_webapp -f
docker-shell:
	docker exec -it lab01_webapp sh