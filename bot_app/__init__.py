import logging
from .app import dp
from . import commands
from .commands import read_one

logging.basicConfig(level=logging.INFO)
