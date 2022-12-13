import sys

from scastpy.servers import http, ssdp
from scastpy.players import FFMpeg, DummyPlayer


def main(host):
    ssdp.run(host)
    http.run(host, player=FFMpeg(output_directory='/Users/ricterz/Desktop/medias'))


if __name__ == '__main__':
    main(host=sys.argv[1])
