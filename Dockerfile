FROM python:3.9


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

EXPOSE 5000
# ENTRYPOINT [ "poetry", "run", "meetup", "serve", "--host", "0.0.0.0"]
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
