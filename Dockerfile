FROM python:3.9-alpine3.13
# use alpine version of python, lightweight image of python

LABEL maintainer="ikehunter.com"
# indicates who maintains this docker image, can just put personal domain

ENV PYTHONUNBUFFERED 1
# dont want to buffer output in console, see logs immediately

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000
# copy requirements, app root, set workdir to app dir, expose port 8000 to local machine

ARG DEV=false
# default dev config is set to false, or prod mode

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        -D \
        -H \
        django-user
# creates a new image layer with multiple commands
# 1. create virtual env
# 2. install and upgrade pip inside virtual env
# 3. install list of requirements in virtual env
    # 3b. install dev requirements if in dev mode
# 4. remove tmp directory to keep it lightweight and clean
# 5. adds new user that is not root user (convention not to use root)
    # 5a. disable password so login is automatic
    # 5b. no need to make new home directory for user, keep lightweight
    # 5c. name the user, can name it anything

ENV PATH="/py/bin:$PATH"
# updates env variable with PATH

USER django-user
# specifies user to switch to, switches from root user to new django-user