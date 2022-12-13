import subprocess
import os
import sys
import threading

from urllib.parse import urlparse
from scastpy.utils.logging import logger
from scastpy.players.base import Player


class FFMpeg(Player):

    uri = None
    filename = None
    output_directory = None

    def __init__(self, output_directory='.', *args, **kwargs):
        try:
            subprocess.Popen(['ffmpeg', '-version'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except Exception as e:
            logger.error('ffmpeg command not found, this player maybe not usable')
            logger.debug(e)

        super().__init__(*args, **kwargs)
        self.output_directory = output_directory

    def stop(self):
        pass

    def get_volume(self):
        return 0

    def set_volume(self, volume):
        pass

    def get_transport_info(self):
        pass

    def get_position_info(self):
        pass

    def set_uri(self, uri):
        self.uri = uri
        self.filename = os.path.basename(urlparse(uri).path)
        logger.info('ffmpeg: {}'.format(uri))

    def play(self):
        logger.info('ffmpeg: starting download video ...')
        if self.uri is None or self.filename is None:
            raise Exception('media uri or output filename not be set')

        # download m3u8 as mp4 file
        _, ext = os.path.splitext(self.filename)
        if ext == '.m3u8' or not ext:
            self.filename += '.mp4'

        output_path = os.path.join(self.output_directory, self.filename)

        # rename if output file exists
        index = 1
        while True:
            if not os.path.exists(output_path):
                break
            fn, ext = os.path.splitext(output_path)
            output_path = fn + '-' + str(index) + ext
            index += 1

        command = ['ffmpeg', '-i', self.uri, '-c', 'copy', output_path]

        def run():
            logger.info('ffmpeg: execute command "{}"'.format(' '.join(command)))
            popen = subprocess.Popen(command,
                                     stdout=subprocess.PIPE, universal_newlines=True)
            for stdout_line in iter(popen.stdout.readline, ""):
                logger.info('ffmpeg: {}'.format(stdout_line))

            popen.stdout.close()
            popen.wait()

        threading.Thread(target=run).start()
