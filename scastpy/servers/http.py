import os.path
import threading

from xml.etree import ElementTree as et
from http.server import BaseHTTPRequestHandler, HTTPServer as HTTPServer_
from scastpy.utils.templates import DESC_TEMPLATE, TEMPLATE_DIR
from scastpy.utils.logging import logger


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

    def log_message(self, _, *args):
        logger.debug('received HTTP request: {}'.format(args[0]))

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/xml')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        if self.path.endswith('ConnectionManager_scpd.xml'):
            with open(os.path.join(TEMPLATE_DIR, 'ConnectionManager.xml'), 'r') as f:
                resp = f.read()
        elif self.path.endswith('RenderingControl_scpd.xml'):
            with open(os.path.join(TEMPLATE_DIR, 'RenderingControl.xml'), 'r') as f:
                resp = f.read()
        elif self.path.endswith('AVTransport_scpd.xml'):
            with open(os.path.join(TEMPLATE_DIR, 'AVTransport.xml'), 'r') as f:
                resp = f.read()
        else:
            resp = DESC_TEMPLATE.format(self.server.host, self.server.port)

        self.wfile.write(resp.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        tree = et.ElementTree(et.fromstring(post_data))
        command = tree.getroot().find('./').find('./')
        response = self.server.player.execute(command)
        self._set_response()
        self.wfile.write(str(response).encode())


def run(host, port=8080, player=None):
    logger.info('starting HTTP server at port {} ...'.format(port))
    server_address = ('', port)
    httpd = HTTPServer(host, server_address, HTTPHandler, player=player)

    threading.Thread(target=httpd.serve_forever).start()
