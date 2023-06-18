import click


@click.group()
def cli():
    """Commands to manipulate todos"""
    pass


@click.command()
def add():
    """Add new todo"""
    click.echo('add')


@click.command()
def list():
    """List todos"""
    click.echo('list')


cli.add_command(add)
cli.add_command(list)