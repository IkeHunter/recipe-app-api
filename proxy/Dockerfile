# secure way to run app, gives nginx only the priveleges it needs.
FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="ikehunter.com"

# copy directories to image
COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

# default env vars
# server listens to 8000, wsgi listens to 9000
ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

# set up image as root user
USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

# user to run application, has less perms
USER nginx

CMD ["/run.sh"]

