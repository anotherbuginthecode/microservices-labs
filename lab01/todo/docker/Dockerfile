# start by pulling the python image
FROM python:3.8-alpine as base
ARG POSTGRES_ENABLED=0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POSTGRES_ENABLED $POSTGRES_ENABLED

RUN addgroup --system web \
    && adduser --system --ingroup web web
USER web
WORKDIR /app
COPY --chown=web:web ./requirements.txt requirements.txt
USER root
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=web:web ./docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
USER web
ENTRYPOINT ["entrypoint.sh"]


FROM base as dev
USER web
WORKDIR /app
COPY --chown=web:web . .
CMD [ "python", "runner.py" ]
