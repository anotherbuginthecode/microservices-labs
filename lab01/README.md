# Microservices lab01

In this laboratory I try to clear my doubts about how to secure services using an authorization and authentication micro-service.

The web app is a simple to-do app where a user can register, add, view and delete tasks.

A micro-service called **todo** was developed to do this.

Any type of interaction with the service is first passed to the authorization service (**auth**) which verifies that the token used is valid, otherwise it will be returned 401.




## Tech Stack

**Client:** Vuejs, TailwindCSS

**Server:** Python, Django, Flask

**Container:** Docker



## Architecture Sample

![Architecture Sample](https://i.imgur.com/GwgKCXT.png)

