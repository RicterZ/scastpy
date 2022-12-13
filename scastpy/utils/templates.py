import os

from scastpy import __version__

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

with open(os.path.join(TEMPLATE_DIR, 'description.xml'), 'r') as f:
    DESC_TEMPLATE = f.read()


SSDP_TEMPLATE = '''HTTP/1.1 200 OK\r
CACHE-CONTROL: max-age=66
DATE: Tue, 13 Dec 2022 05:39:15 GMT
EXT:
LOCATION: {location}\r
OPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01
01-NLS: ee9ae638-1dd1-11b2-99a1-cb4ea77414bd
SERVER: ScastPy/{VERSION} HTTP/1.0
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

