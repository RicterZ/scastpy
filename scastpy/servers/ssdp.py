import socket
import struct
import threading

from uuid import uuid4
from socketserver import BaseRequestHandler, UDPServer
from scastpy.utils.templates import SSDP_TEMPLATE
from scastpy.utils.logging import logger


TYPES = (
    'upnp:rootdevice',
    '',
    'urn:schemas-upnp-org:device:MediaRenderer:1',
    'urn:schemas-upnp-org:service:AVTransport:1',
    'urn:schemas-upnp-org:service:RenderingControl:1',
    'urn:schemas-upnp-org:service:ConnectionManager:1',
)


class SSDPHandler(BaseRequestHandler):
    server = None

    def make_payload(self):
        original_usn = 'uuid:{}'.format(self.server.uuid)
        for type_ in TYPES:
            if type_ != '':
                usn = original_usn + '::' + type_
                st = type_
            else:
                usn = original_usn
                st = usn

            data = SSDP_TEMPLATE.format(location=self.server.location, st=st, usn=usn)
            yield data

    def handle(self):
        logger.debug('received SSDP request from {}:{}'.format(*self.client_address))

        msg, sock = self.request

        if self.server.uuid is None or self.server.location is None:
            raise Exception('uuid or location not set')

        for data in self.make_payload():
            sock.sendto(data.encode(), self.client_address)


class SSDPServer(UDPServer):
    uuid = None
    location = None
    allow_reuse_address = True

    def __init__(self, location, uuid=None):
        self.location = location

        if uuid is None:
            self.uuid = str(uuid4())

        super(SSDPServer, self).__init__(('', 1900), SSDPHandler, bind_and_activate=False)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        self.socket.bind(self.server_address)
        mreq = struct.pack('4sl', socket.inet_aton('239.255.255.250'), socket.INADDR_ANY)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


def run(host, port=8080):
    logger.info('starting SSDP server ...')
    server = SSDPServer('http://{}:{}/description.xml'.format(host, port))
    threading.Thread(target=server.serve_forever).start()
