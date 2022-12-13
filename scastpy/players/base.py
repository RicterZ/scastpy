import re

from scastpy.utils.logging import logger
from scastpy.utils.templates import RESPONSE_TEMPLATE


class Player(object):
    MATCH_COMMAND = re.compile('\{(.*?)\}(.*)')

    def __init__(self, *args, **kwargs):
        logger.info('player {} loaded successfully'.format(self.__class__.__name__))

    def make_response(self, command, namespace, response):
        if response is None:
            response = ''
        resp = RESPONSE_TEMPLATE.format(ACTION=command, NS=namespace, RESPONSE=response)
        return resp

    def execute(self, tag):
        namespace, cmd = self.MATCH_COMMAND.findall(tag.tag)[0]
        logger.debug('received player command: {}'.format(cmd))

        command = cmd.upper()
        resp = None
        if command == 'STOP':
            self.stop()
        elif command == 'PLAY':
            self.play()
        elif command == 'SETAVTRANSPORTURI':
            uri = tag.find('./CurrentURI').text.strip()
            self.set_uri(uri)
        elif command == 'GETVOLUME':
            resp = int(self.get_volume())
            resp = '<CurrentVolume>{}</CurrentVolume>'.format(resp)
        elif command == 'SETVOLUME':
            volume = tag.find('./DesiredVolume').text.strip()
            self.set_volume(volume=volume)
        elif command == 'GETTRANSPORTINFO':
            resp = self.get_transport_info()
        elif command == 'GETPOSITIONINFO':
            resp = self.get_position_info()
        else:
            logger.info('unexpected command: {}'.format(tag.tag))

        return self.make_response(cmd, namespace, resp)

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


