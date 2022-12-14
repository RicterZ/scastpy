import os

from scastpy import __version__

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

with open(os.path.join(TEMPLATE_DIR, 'description.xml'), 'r') as f:
    DESC_TEMPLATE = f.read()


SSDP_NOTIFY_TEMPLATE = '''NOTIFY * HTTP/1.1\r
HOST: 239.255.255.250:1900\r
CACHE-CONTROL: max-age=66\r
LOCATION: {location}\r
OPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01\r
01-NLS: {uuid}\r
NT: {st}\r
NTS: ssdp:alive\r
SERVER: ScastPy/{VERSION} HTTP/1.0\r
X-User-Agent: ssdpy\r
USN: {usn}\r
\r
'''.replace('{VERSION}', __version__)


SSDP_RESPONSE_TEMPLATE = '''HTTP/1.1 200 OK\r
CACHE-CONTROL: max-age=66\r
DATE: {{DATE}}\r
EXT:\r
LOCATION: {location}\r
OPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01\r
01-NLS: {uuid}\r
SERVER: ScastPy/{VERSION} HTTP/1.0\r
X-User-Agent: scastpy\r
ST: {st}\r
USN: {usn}\r
\r
'''.replace('{VERSION}', __version__)

RESPONSE_TEMPLATE = '''<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
  s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <s:Body>
    <u:{ACTION}Response xmlns:u="{NS}">
        {RESPONSE}
    </u:{ACTION}Response>
  </s:Body>
</s:Envelope>'''

