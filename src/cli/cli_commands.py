from typing import Optional

import typer

cli_app = typer.Typer()


@cli_app.callback()
def before_commands():
    pass


@cli_app.command("create_database")
def _create_database(
    create_tables: Optional[bool] = typer.Option(default=True),
    init_database: Optional[bool] = typer.Option(default=False, prompt=True),
) -> None:
    """Initialize the DB, required creating tables and optionally inserting data."""
    if create_tables:
        print("to_create_tables()")
    if init_database:
        print("to_insert_data()")


if __name__ == "__main__":
    cli_app()
