# Intro
This respository contains the basic Python architecture based on [nginx](http://nginx.org/en/), [gunicorn](http://gunicorn.org/) and [flask](http://flask.pocoo.org/) inside docker containers. Feel free to use it!! 

# How to run it
You have to have installed [docker](https://www.docker.com/) in other to make it work.

## Create docker machine
    $ docker-machine create -d virtualbox dev

## Enable docker machine
    $ eval "$(docker-machine env dev)"
    
## Run the service
    $ docker-compose build
    $ docker-compose up -d

## To view the logs
    $ docker-compose logs

## If you want to access to the containers
    $ docker exec -it <containerIdOrName> bash