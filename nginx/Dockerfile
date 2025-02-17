FROM nginx:alpine

RUN addgroup -S nonroot \
    && adduser -S nonroot -G nonroot

USER nonroot

COPY ./default.conf /etc/nginx/conf.d/default.conf
