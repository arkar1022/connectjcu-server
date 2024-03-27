FROM nginx:mainline-alpine3.18-perl
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./cert_chain.crt ./etc/nginx/cert_chain.crt
COPY ./server.key ./etc/nginx/server.key