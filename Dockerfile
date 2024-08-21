FROM postgres:15

ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=12345
ENV POSTGRES_DB=test_db

VOLUME /test:/var/lib/postgresql/data
