# Lab01

In this workshop I try to clear my doubts about how to secure services using an authorization and authentication microservice.

The web app is a simple to-do app where a user can register a new account, add, view and delete tasks.

A microservice called **todo** was developed to do this.

Any type of interaction with the service is first passed to the authorization service (**auth**) which verifies that the token used is valid, otherwise it will be returned 401.

![architecture](https://i.imgur.com/PCYVBVF.png)


## Tech Stack

**Frontend:** Vuejs, TailwindCSS

**Backend:** Python 3+, Django, Flask

**Container:** Docker, docker-compose

## How to use

**Build all images**

Before starting, you have to build all images. Inside each microservice there is a **Makefile**.
~~~
cd microservice-folder/
make docker-build

# or something likes

docker build . -f docker/Dockerfile -t msalab01/auth:v1
~~~

In alternative you can run the bash script **bootstrap.sh** to do the dirty job for you!

~~~
./bootstrap.sh #or bash bootstrap.sh
~~~

It will build the corresponding image.

**Run all microservices at once**

Once done, go back to the root folder and run the command:
~~~
make start 
# or 
doocker-compose up -d
~~~

All services should go up!

![screenshot](https://i.imgur.com/uP5IDOi.png)

To use the webapp connect to **localhost:80** or **localhost** in your browser.


