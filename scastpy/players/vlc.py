import vlc

from scastpy.players.base import Player
from scastpy.utils.logging import logger


class VLCPlayer(Player):
    media = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.media = vlc.MediaPlayer()

    def set_uri(self, uri):
        logger.info('VLC player: {}'.format(uri))
        self.media.set_mrl(uri)

    def play(self):
        logger.info('VLC player: playing')
        self.media.play()

    def stop(self):
        logger.info('VLC player: stopped')
        self.media.stop()

    def set_volume(self, volume):
        logger.info('VLC player: set volume to {}'.format(volume))
        self.media.audio_set_volume(int(volume))

    def get_volume(self):
        return self.media.audio_get_volume()

    def get_position_info(self):
        return self.media.get_position()

    def get_transport_info(self):
        pass


