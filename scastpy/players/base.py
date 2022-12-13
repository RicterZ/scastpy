import re

from scastpy.utils.logging import logger


class Player(object):
    MATCH_COMMAND = re.compile('\{.*?\}(.*)')

    def __init__(self, *args, **kwargs):
        pass

    def execute(self, tag):
        command = self.MATCH_COMMAND.findall(tag.tag)[0]
        logger.debug('received player command: {}'.format(command))
        command = command.upper()

        if command == 'STOP':
            self.stop()
        elif command == 'PLAY':
            self.play()
        elif command == 'SETAVTRANSPORTURI':
            uri = tag.find('./CurrentURI').text.strip()
            self.set_uri(uri)
        elif command == 'GETVOLUME':
            return self.get_volume()
        elif command == 'SETVOLUME':
            volume = tag.find('./DesiredVolume').text.strip()
            self.set_volume(volume=volume)
        elif command == 'GETTRANSPORTINFO':
            return self.get_transport_info()
        elif command == 'GETPOSITIONINFO':
            return self.get_position_info()
        else:
            logger.info('unexpected command: {}'.format(tag.tag))

    def stop(self):
        raise NotImplementedError

    def play(self):
        raise NotImplementedError

    def set_uri(self, uri):
        raise NotImplementedError

    def get_volume(self):
        raise NotImplementedError

    def set_volume(self, volume):
        raise NotImplementedError

    def get_transport_info(self):
        raise NotImplementedError

    def get_position_info(self):
        raise NotImplementedError


