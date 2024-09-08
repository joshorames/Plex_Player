import board, neopixel
import time
from urllib.request import Request, urlopen
from plexapi.myplex import MyPlexAccount
account = MyPlexAccount('', '')
plex = account.resource('Josh comp').connect()
print(plex.playlist('weird sounds').duration)
playlist_duration = plex.playlist('weird sounds').duration

def led_circle(led, loop_num):
        for x in range(16):
                led[x]=(255,255,255)
                time.sleep(1)

playlist_dict = {
    '1': ''
}

led = neopixel.NeoPixel(board.D18, 16)

led_circle(led,2)

white = (255,255,255)
led.fill(white)

choice = input()

if choice in playlist_dict:
        while True:
                req = Request(
                        url=playlist_dict[choice],
                        headers={'User-Agent': 'Mozilla/5.0'})
                with urlopen(req) as response:
                        body = response.read()
                time.sleep(playlist_duration/1000)








