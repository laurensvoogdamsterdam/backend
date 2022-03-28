import click
import uvicorn


@click.group()
@click.version_option()
def cli() -> None:
    """Command line interface for the recommender model."""


@cli.command()
@click.option("--title", default="API")
@click.option("--host", default="0.0.0.0")
@click.option("--port", default=5001)
@click.option("--debug/--no-debug", default=False)
def serve(title: str, host: str, port: int, debug: bool) -> None:
    """Serves a fitted model in a REST API."""
    # from .app import GroupRecommender

    uvicorn.run("backend.api:api", host=host, port=port, reload=True, workers=2)


@cli.command()
def train() -> None:
    """Train and save model to disk."""
    pass


if __name__ == "__main__":
    cli()
