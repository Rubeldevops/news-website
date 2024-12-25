FROM mariadb:10.5

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=news

COPY init.sql /docker-entrypoint-initdb.d/
