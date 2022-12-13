import logging
import sys

from scastpy.servers import http, ssdp
from scastpy.players.dummy import DummyPlayer


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(fmt="%(asctime)s [%(filename)s] %(levelname)s: %(message)s",
                              datefmt="%Y/%m/%d %H:%M:%S")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


def main(host):
    ssdp.run(host)
    http.run(host, player=DummyPlayer())


if __name__ == '__main__':
    main(host=sys.argv[1])
