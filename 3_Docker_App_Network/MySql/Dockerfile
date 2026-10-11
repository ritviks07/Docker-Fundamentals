FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=demopassword
ENV MYSQL_DATABASE=demodb

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3307

