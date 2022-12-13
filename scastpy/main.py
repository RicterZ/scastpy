import sys

from scastpy.servers import http, ssdp
from scastpy.players.dummy import DummyPlayer


def main(host):
    ssdp.run(host)
    http.run(host, player=DummyPlayer())


if __name__ == '__main__':
    main(host=sys.argv[1])
