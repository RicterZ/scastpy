import socket
import struct
import time
import threading

from uuid import uuid4
from email.utils import formatdate
from socketserver import BaseRequestHandler, UDPServer
from scastpy.utils.templates import SSDP_RESPONSE_TEMPLATE, SSDP_NOTIFY_TEMPLATE
from scastpy.utils.logging import logger


TYPES = (
    'upnp:rootdevice',
    '',
    'urn:schemas-upnp-org:device:MediaRenderer:1',
    'urn:schemas-upnp-org:service:AVTransport:1',
    'urn:schemas-upnp-org:service:RenderingControl:1',
    'urn:schemas-upnp-org:service:ConnectionManager:1',
)


def make_payload(uuid, uuid2, location, template):
    original_usn = 'uuid:{}'.format(uuid)
    for type_ in TYPES:
        if type_ != '':
            usn = original_usn + '::' + type_
            st = type_
        else:
            usn = original_usn
            st = usn

        data = template.format(location=location, st=st, usn=usn, uuid=uuid2)
        data = data.replace('{DATE}', formatdate(timeval=None, localtime=False, usegmt=True))
        yield data


class SSDPHandler(BaseRequestHandler):
    server = None

    def handle(self):
        msg, sock = self.request
        if msg.decode().startswith('NOTIFY'):
            return

        logger.debug('received SSDP request from {}:{}'.format(*self.client_address))
        if self.server.uuid is None or self.server.location is None:
            raise Exception('uuid or location not set')

        for data in make_payload(self.server.uuid, self.server.uuid2,
                                 self.server.location, SSDP_RESPONSE_TEMPLATE):
            sock.sendto(data.encode(), self.client_address)


class SSDPServer(UDPServer):
    uuid = None
    uuid2 = None
    location = None
    allow_reuse_address = True

    def __init__(self, location, uuid=None, auto_discover=False):
        self.location = location

        if uuid is None:
            self.uuid = str(uuid4())

        self.uuid2 = str(uuid4())
        super(SSDPServer, self).__init__(('', 1900), SSDPHandler, bind_and_activate=False)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        self.socket.bind(self.server_address)
        req = struct.pack('4sl', socket.inet_aton('239.255.255.250'), socket.INADDR_ANY)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req)

        if auto_discover:
            logger.info('starting auto discover service ...')
            threading.Thread(target=self.auto_discover).start()

    def auto_discover(self):
        while True:
            logger.debug('sending NOTIFY multicast message ...')
            for data in make_payload(self.uuid, self.uuid2,
                                     self.location, SSDP_NOTIFY_TEMPLATE):
                self.socket.sendto(data.encode(), ('239.255.255.250', 1900))
            time.sleep(1)


def run(host, port=8080):
    logger.info('starting SSDP server ...')
    server = SSDPServer('http://{}:{}/description.xml'.format(host, port))
    threading.Thread(target=server.serve_forever).start()
