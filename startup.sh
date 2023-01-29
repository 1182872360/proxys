#!/usr/bin/env bash

#===================================================================#
#   Author: luolongfei <luolongf@gmail.com>                         #
#   Intro: https://github.com/luolongfei/freenom                    #
#===================================================================#

set -e

# 替换端口变量

# 启动 php-fpm 与 nginx
nohub python /app/proxy.py &; nginx -c /app/nginx.template.conf -g 'daemon off;'
