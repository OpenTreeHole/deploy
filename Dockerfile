FROM nginx:alpine

MAINTAINER jsclndnz@gmail.com

WORKDIR /etc/nginx

COPY nginx.conf /etc/nginx
COPY default.conf /etc/nginx/conf.d
COPY treehole.conf.template /etc/nginx/templates/

EXPOSE 80
EXPOSE 443


