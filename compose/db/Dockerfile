FROM postgres:15

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

COPY ./compose/db/init.sql /docker-entrypoint-initdb.d/
