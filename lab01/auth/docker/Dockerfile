FROM python:3.8 as base

ARG POSTGRES_ENABLED=0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POSTGRES_ENABLED=$POSTGRES_ENABLED

RUN addgroup --system web \
    && adduser --system --ingroup web web

RUN apt-get update && apt-get install -y -q --no-install-recommends \
  build-essential \
  libpq-dev \
  # cleaning up unused files to reduce the image size
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

USER web
WORKDIR /home/web/code/
COPY --chown=web:web ../requirements.txt requirements.txt

USER root
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=web:web ./docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
USER web
ENTRYPOINT ["entrypoint.sh"]


FROM base as dev
COPY --chown=web:web ./docker/start-server.sh /usr/local/bin/start-server.sh
USER root
RUN chmod +x /usr/local/bin/start-server.sh
USER web
COPY --chown=web:web . ./

CMD ["start-server.sh"]