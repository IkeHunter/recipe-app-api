#!/bin/sh

set -e

# substitute variables in conf file with env varialbes.
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
# start nginx with config, run daemon in foreground due to it being in docker container
nginx -g 'daemon off;'
