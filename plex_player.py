import board, neopixel
import sys
import os
import time
from urllib.request import Request, urlopen
from plexapi.myplex import MyPlexAccount

account = MyPlexAccount('', '')
plex = account.resource('Josh comp').connect()
print(plex.playlist('weird sounds').duration)
playlist_duration = plex.playlist('weird sounds').duration

led_num = 16

def led_clr(led):
    for x in range(led_num):
        led[x]=(0,0,0)

def led_circle(led, loop_num, color):
    for x in range(led_num):
        led_clr(led)
        led[x]=color
        time.sleep(20/1000)

def led_pulse(led, loop_num, color):
    for x in range(led_num):
        led[x]=color
    time.sleep(3)
    led_clr(led)

led = neopixel.NeoPixel(board.D18, led_num)

ring_dict = {
    'scanned_success': (0,128,0),
    'scanned_failed': (128,0,0),
    '1': (255,255,255),
    '2': (173,216,230)
}

playlist_dict = {
    '1': ''
}

choice = input()

if choice in playlist_dict:
    led_circle(led,2,ring_dict['scanned_success'])
    while True:
        req = Request(
            url=playlist_dict[choice],
            headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as response:
            body = response.read()
        time.sleep(playlist_duration/1000)
else:
    led_pulse(led,2,ring_dict['scanned_failed'])





