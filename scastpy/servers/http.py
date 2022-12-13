import logging
import threading

from xml.etree import ElementTree as et
from http.server import BaseHTTPRequestHandler, HTTPServer as HTTPServer_
from scastpy.templates import HTTP_TEMPLATE, COMMON_RESPONSE

logger = logging.getLogger()


class HTTPServer(HTTPServer_):
    host = None
    port = None
    player = None

    def __init__(self, host, addr, cls, player):
        self.host = host
        self.port = addr[1]
        self.player = player
        super(HTTPServer, self).__init__(addr, cls)


class HTTPHandler(BaseHTTPRequestHandler):
    server = None

    def log_message(self, format, *args):
        logger.debug('received HTTP request: {}'.format(args[0]))

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/xml')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        resp = HTTP_TEMPLATE.format(self.server.host, self.server.port).encode()
        self.wfile.write(resp)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        tree = et.ElementTree(et.fromstring(post_data))
        command = tree.getroot().find('./').find('./')
        response = self.server.player.execute(command)
        if response is None:
            response = COMMON_RESPONSE

        self._set_response()
        self.wfile.write(str(response).encode())


def run(host, port=8080, player=None):
    logger.info('starting HTTP server at port {} ...'.format(port))
    server_address = ('', port)
    httpd = HTTPServer(host, server_address, HTTPHandler, player=player)

    threading.Thread(target=httpd.serve_forever).start()
