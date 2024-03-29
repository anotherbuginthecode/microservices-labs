
![Banner](https://i.imgur.com/qiLTkD9.png)

<p float="middle">
  <img src="https://img.shields.io/github/last-commit/anotherbuginthecode/microservices-labs?style=flat-square" style="margin-left: 10px;" />
  <img src="https://img.shields.io/github/forks/anotherbuginthecode/microservices-labs?style=flat-square" style="margin-left: 10px;"/>
  <img src="https://img.shields.io/github/stars/anotherbuginthecode/microservices-labs?style=flat-square" style="margin-left: 10px;"/>
</p>

A series of experiements while I'm learning about microservices architecture.

Sometimes I come across articles or videos where microservice architecture is discussed, and each time I am fascinated.

I like the idea that I can share with you my journey of experimenting, asking questions and trying to give myself answers. Maybe you can find something useful here (or maybe not). There is always something to learn from everyone.

Each Lab tries to give an answer to a doubt I have, I hope to solve yours as well.

Explanations of my labs can be found on [medium](https://medium.com/@anotherbuginthecode), follow me so you can be sure to stay updated when a new lab pops up!



## Lab01

In this laboratory I try to clear my doubts about how to secure services using an authorization and authentication microservice.

The web app is a simple to-do app where a user can register an account, add, view and delete tasks.

A microservice called **todo** was developed to do this.

Any type of interaction with the service is first passed to the authorization service (**auth**) which verifies that the token used is valid, otherwise it will be returned 401.

[![Buymeacoffee](https://i.imgur.com/PcXxuL3.png)](https://www.buymeacoffee.com/mangonedev)
