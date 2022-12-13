from scastpy.players.base import Player
from scastpy.utils.logging import logger


class DummyPlayer(Player):
    def stop(self):
        logger.info('dummy player: stopped')

    def play(self):
        logger.info('dummy player: playing')

    def set_uri(self, uri):
        logger.info(uri)

    def get_volume(self):
        logger.info('dummy player: get volume')
        return 10

    def set_volume(self, volume):
        logger.info('dummy player: set volume to {}'.format(volume))

    def get_position_info(self):
        return 'XXX'

    def get_transport_info(self):
        return 'XXX'


