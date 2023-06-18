import click


@click.command()
def add():
    """Add new todo"""
    click.echo('add')


@click.command()
def list_all():
    """List todos"""
    click.echo('list')


@click.group()
def setup_cli():
    """Commands to manipulate todos"""
    pass


setup_cli.add_command(add)
setup_cli.add_command(list_all)


if __name__ == '__main__':
    setup_cli()
