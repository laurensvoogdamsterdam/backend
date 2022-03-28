# Backend API - Starter

# Introduction

# Project Structure & Features

The project works with [`Github Action`](https://github.com/features/actions) for CI/CD.
The workflow contains the following steps:

- Lint & Format code
- Test code using pytes
- Build Docker image CI
- Deploy documentation to [`Firebase`](https://firebase.google.com/?gclid=CjwKCAiA-9uNBhBTEiwAN3IlNAYf7X_O7obqw9YIJ0h3apAVRxVMemE1VZS2EJbWXYxwj9oGThF1HxoCPkoQAvD_BwE&gclsrc=aw.ds)
- Publisch package to [`PyPi`](https://pypi.org/%27)
- Build, push and deploy Docker image to [`Google Container Registry (gcr)`](http://cloud.google.com/container-registry)
- Deploy (load balanced) recommender app to [`Kubernetes`](https://cloud.google.com/kubernetes-engine/docs)

# Quick Start

Make sure [`poetry`](https://python-poetry.org/) is installed and install all (development) dependencies:

```sh
poetry install
```

Set up [`pre-commit`](https://pre-commit.com/):

```sh
poetry run pre-commit install
```

... and you should be all set up!

Check `.pre-commit-config.yaml` for all linters, formatters, etc.

In case you want to trigger them manually, run:

```sh
poetry run pre-commit run --all-files
```

## Running the API from Python

Run the API directly with:

```sh
poetry run backend serve
```

## Running the API with Docker

Make sure your Docker daemon is running and build the image:

```sh
docker build --tag meetup .
```

Met het vliegtui auto of de boot eindigen Donna Golli en Kaaje na wat Sangria geregeld in de Spaanse goot.

Run the container:

```sh
docker run --rm -p 5000:5000 meetup
```

If you navigate to [http://localhost:5000/api/v1/ping](http://localhost:5000/api/v1/ping), you should see the 'pong' response.
