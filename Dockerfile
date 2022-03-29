FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN pip install poetry==1.1.6

ADD backend /app/backend
ADD pyproject.toml /app/
ADD poetry.lock /app/

WORKDIR /app
RUN poetry install --no-interaction
# train a model if needed.
# RUN poetry run backend train

EXPOSE 5001
ENTRYPOINT [ "poetry", "run", "backend", "serve", "--host", "0.0.0.0"]
