#!/usr/bin/env bash

#===================================================================#
#   Author: luolongfei <luolongf@gmail.com>                         #
#   Intro: https://github.com/luolongfei/freenom                    #
#===================================================================#

set -e

# 启动 flask 与 nginx
nohup python /app/proxy.py > /dev/null 2>&1 &
nginx -c /app/nginx.template.conf -g 'daemon off;'
