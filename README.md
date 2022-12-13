ScastPy
=======
ScastPy is a digital media player written by Python, which can receive and handle screencast requests from mobile phone applications.  

### Usage
```
Usage: scastpy -l [ip] -p [player]

Options:
  -h, --help            show this help message and exit
  -l HOST, --local=HOST
                        the local ip address
  --port=PORT           listening port of HTTP service
  -p PLAYER, --player=PLAYER
                        the player to use
  -c CONFIG, --config=CONFIG
                        config string for player
  --loglevel=LOGLEVEL   set logging level for debugging
```

Example: use ffmpeg as player and set output directory.
```bash
$ scastpy -l 192.168.1.2 -p ffmpeg -c output_directory=/tmp --loglevel DEBUG
```

### Supported Players
Player is a backend can handle DLNA actions, but also can perform download or video codec.

- [vlc](https://www.videolan.org/): Provide a user interface to play videos
- [ffmpeg](https://ffmpeg.org/): Use ffmpeg to download videos
- dummy: For testing and development

### Supported Clients
- [x] Bilibili
- [x] Baidu NetDisk
- [x] iQiyi
- [ ] AirPlay