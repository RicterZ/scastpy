import inspect
import sys

from scastpy.utils.logging import logger
from scastpy.players.dummy import DummyPlayer
from scastpy.players.vlc import VLCPlayer
from scastpy.players.ffmpeg import FFMpeg


def find_player(name):
    for _, cls in inspect.getmembers(sys.modules['scastpy.players'], inspect.isclass):
        if cls.name == name:
            return cls

    logger.error('player {} not found'.format(name))
    sys.exit(1)
