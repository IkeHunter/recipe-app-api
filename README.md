# recipe-app-api
Recipe API personal project

## Technologies
* Docker
* Python (alpine image)
* Flake8 for linting
* Django test suite for unite tests

## Terminal Commands
To build docker image after creating dockerfile:

    docker build .

To build docker-compose after docker-compose.yml creation:

    docker-compose build

Run code with linting:

    docker-compose run --rm app sh -c "flake8"

Run code with test suite

    docker-compose run --rm app sh -c "python manage.py test"

Create Django Project with Docker in CLI

    docker-compose run --rm app sh -c "django-admin startproject app ."

Run local DEV server to view in browser (runs services)

    docker-compose up

Stop Server: 

    [press ^c on keyboard]


## Setup Guide
1. Created new git project
    * created new git secret vars for docker
2. Wrote requirements.txt
3. Created Dockerfile
    * set python image
    * set label and env settings
    * establish requirements file, workdir, and port
    * write run script that installs requirements and creates user
    * set path var
    * switches from root user to new user
4. Create docker-compose.yml
    * establishes services
    * sets dev/prod state
    * sets port
    * links local system with image, 2 way auto update
    * set python runserver command
5. Set up linking and test suite
    * create requirements.dev.txt
    * link requirements.dev.txt to dockerfile, create DEV var and script if statement
    * create app/.flake8 file to establish flake version, manage excludes
    * run *"Run code with linting"* command to test
6. Create Django project with CLI command *"Create Django Project with Docker in CLI"* to create Django base project in docker image, this will copy to local system in app/ dir
7. Run project with docker compose with *docker-compose up*