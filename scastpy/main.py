import sys

from optparse import OptionParser

from scastpy.servers import http, ssdp
from scastpy.players import find_player
from scastpy.utils.logging import logger


def cmdline():
    parser = OptionParser('scastpy -l [ip] -p [player]')
    parser.add_option('--local', '-l', action='store', dest='host',
                      help='the local ip address')
    parser.add_option('--player', '-p', action='store', dest='player',
                      help='the player to use', default='dummy')
    parser.add_option('--config', '-c', action='store', dest='config',
                      help='config string for player')
    parser.add_option('--loglevel', action='store', dest='loglevel',
                      help='set log level', default='INFO', choices=('DEBUG', 'INFO'))
    args, _ = parser.parse_args(sys.argv[1:])

    if not args.host:
        parser.print_help()
        sys.exit(1)

    config = {}
    if args.config:
        configs = str(args.config).split(',')
        for c in configs:
            k, v = c.split('=', 1)
            config[k] = v

        args.config = config

    if args.loglevel:
        logger.setLevel(args.loglevel)

    return args


def main():
    args = cmdline()

    player_cls = find_player(args.player)
    ssdp.run(args.host)
    http.run(args.host, player=player_cls(**args.config))


if __name__ == '__main__':
    main()
