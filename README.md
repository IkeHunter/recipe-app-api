# recipe-app-api
Recipe API personal project

## Technologies
* Docker
* Python (alpine image)
* Flake8 for linting
* Django test suite for unite tests

## Terminal Commands
### Docker Mangement
To build docker image after creating dockerfile:
```sh
docker build .
```
To build docker-compose after docker-compose.yml creation:
```sh
docker-compose build
```
### Linting and Testing
Run code with linting:
```sh
docker-compose run --rm app sh -c "flake8"
```
```sh
docker-compose run --rm app sh -c "[command] && flake8"
# ex: "python manage.py wait_for_db && flake8"
```
Run code with test suite
```sh
docker-compose run --rm app sh -c "python manage.py test"
```
### App and Project Creation
Create Django Project with Docker in CLI
```sh
docker-compose run --rm app sh -c "django-admin startproject app ."
```
Create Django App with Docker in CLI
```sh
docker-compose run --rm app sh -c "django-admin startapp core"
```

### Developing Commands
Run local DEV server to view in browser (runs services)
```sh
docker-compose up
```
Stop Server:
```sh
[press ^c on keyboard]
```

Wait for db then apply migrations
```sh
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
```

Remove docker volume:
```sh
docker volume ls  # list volumes

docker volume rm [volume]  # remove specified volume
```

## Setup Guide
### Initial Setup
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

### Creating DB and App
At this point you will have a Django *project*, but in order to create the main functionality you will need to create an *app* within the project.

8. Define `db` service in `docker-compose.yml`. This will configure the postgres db in docker.
9. Add dependencies for `psycopg2` in `Dockerfile` (using the apk add/del commands). Add psycopg2 to `requirements.txt`.
10. Configure db with django, it needs to know: engine, hostname, port, db name, username, password (by using env vars, match service config). This is all configured in `settings.py`. Remove config for original db (sqlite), replace with postgres data.
11. Create new django Core app using *Create Django App with Docker in CLI* command. Clean up app by configuring tests, etc. Add Core app to `settings.py`.
12. Create `wait_for_db` command by creating `/management/commands/[command].py` file inside core
13. Add `wait_for_db` command and `migrate` command to `docker-compose.yml`.

## Explanations

### For testing command
```sh
docker-compose run --rm app sh -c "python manage.py test"
```
docker-compose run: this is the run command in docker compose

### Django ORM
> ORM: Object Relational Mapper

Django handles db structure, changes
When you create a model in Django, it will automatically go through the following steps:
1. Genearate migration files
2. Setup database
3. Store the data

Models:
- each map to table
- contain name, fields, metadata
- can contain custom logic

Migrations:
- ensure app is enabled in `settings.py`
- use django cli:
```sh
python manage.py makemigrations  # create migrations

python manage.py migrate  # applies migrate files to db, run after wait_for_db
```
### DB with Psycopg2
This is Django's preferred package to use to connect with postgres. For dev, installing the binary version is the recommended, but installing the base version is the recommended version for prod. The base version is a bit more difficult to install due to it's dependencies, and may need trial and error to work on occasion.

It is recommended that the packages needed for it's install are deleted after install.

## Bugs

### psycopg2 not found
> Reference: https://github.com/psycopg/psycopg2/issues/684

This issue happened when trying to run/build docker for the first time with psycopg2
These were the original temp packages that should've been installed: `build-base` `postgresql-dev` `musl-dev`
These are the packages that allowed docker to run: `postgresql-dev` `gcc` `python3-dev` `musl-dev`

