""" Command Line Interface for PyHAPWoL """
import click
from logging import basicConfig, DEBUG, INFO
from yaml import load
from yaml.loader import SafeLoader
from .bridge import start
from . import __version__


@click.command()
@click.option('--config', '-c', default='config.yaml', show_default=True,
              help='Configuration file to use.')
@click.option('--state', '-s', default='homekit.state', show_default=True,
              help='HomeKit State file for persistence.')
@click.option('--debug', '-d', default=False, is_flag=True, show_default=False,
              type=click.BOOL, help='Set log level to Debug.')
@click.version_option(__version__, prog_name='pyhapwol')
def main(config, state, debug):
    """Start HomeKit Server with specified configuration and state file."""

    if debug:
        basicConfig(level=DEBUG)
    else:
        basicConfig(level=INFO)
    cfg = {}
    with open(config, 'r') as file:
        cfg = load(file, Loader=SafeLoader)

    start(cfg, state)


if __name__ == '__main__':
    main()
