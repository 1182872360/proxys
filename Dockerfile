FROM python:3.10-alpine

ENV TZ Asia/Shanghai

WORKDIR /app

COPY . ./

COPY ./nginx.template.conf ./

RUN set -eux \
    && apk update \
    && apk add --no-cache tzdata bash nginx gettext

COPY ./heroku/startup.sh /
RUN chmod +x /startup.sh

# https://devcenter.heroku.com/articles/container-registry-and-runtime#dockerfile-commands-and-runtime
CMD ["/bin/bash", "-c", "/startup.sh"]
