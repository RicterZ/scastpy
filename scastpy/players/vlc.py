import subprocess

from scastpy.players.base import Player
from scastpy.utils.logging import logger


class VLCPlayer(Player):
    name = 'vlc'
    uri = None
    process = None

    def __init__(self, *args, **kwargs):
        try:
            subprocess.Popen(['vlc', '--version'], stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        except Exception as e:
            logger.error('vlc command not found, this player maybe not work')
            logger.debug(e)

        super().__init__(*args, **kwargs)

    def set_uri(self, uri):
        logger.info('VLC player: {}'.format(uri))
        self.uri = uri

    def play(self):
        logger.info('VLC player: playing')
        self.process = subprocess.Popen(['vlc', '--fullscreen', self.uri])

    def stop(self):
        logger.info('VLC player: stopped')
        self.process.kill()

    def pause(self):
        logger.info('VLC player: pause not be supported')

    def set_volume(self, volume):
        logger.info('VLC player: set volume to {} not be supported'.format(volume))

    def get_volume(self):
        return 0

    def get_position_info(self):
        pass

    def get_transport_info(self):
        pass


