import time
import http.client
import pygame

timez = 1.9
playnum = 0

pygame.mixer.init()
pygame.mixer.music.load("Project2Test.mp3")

def green():
    conn = http.client.HTTPSConnection("io.adafruit.com")

    payload = "{\n  \"value\": \"#0aff00\"\n}"

    headers = {
        'content-type': "application/json",
        'x-aio-key': "cc7c424522214ee6ae2106eebed45135"
        }

    conn.request("POST", "/api/v2/kvnkey/feeds/color/data", payload, headers)

    #res = conn.getresponse()
    #data = res.read()

    print("Green!")
    #print(data.decode("utf-8"))
    print("\n")

def red():
    conn = http.client.HTTPSConnection("io.adafruit.com")

    payload = "{\n  \"value\": \"#ff0000\"\n}"

    headers = {
        'content-type': "application/json",
        'x-aio-key': "cc7c424522214ee6ae2106eebed45135"
        }

    conn.request("POST", "/api/v2/kvnkey/feeds/color/data", payload, headers)

    #res = conn.getresponse()
    #data = res.read()

    print("Red!")
    #print(data.decode("utf-8"))
    print("\n")

def yellow():
    conn = http.client.HTTPSConnection("io.adafruit.com")

    payload = "{\n  \"value\": \"#f8ff00\"\n}"

    headers = {
        'content-type': "application/json",
        'x-aio-key': "cc7c424522214ee6ae2106eebed45135"
        }

    conn.request("POST", "/api/v2/kvnkey/feeds/color/data", payload, headers)

    #res = conn.getresponse()
    #data = res.read()

    print("Yellow!")
    #print(data.decode("utf-8"))
    print("\n")

def blue():
    conn = http.client.HTTPSConnection("io.adafruit.com")

    payload = "{\n  \"value\": \"#0037ff\"\n}"

    headers = {
        'content-type': "application/json",
        'x-aio-key': "cc7c424522214ee6ae2106eebed45135"
        }

    conn.request("POST", "/api/v2/kvnkey/feeds/color/data", payload, headers)

    #res = conn.getresponse()
    #data = res.read()

    print("Blue!")
    #print(data.decode("utf-8"))
    print("\n")

def playon():
    conn = http.client.HTTPSConnection("io.adafruit.com")

    payload = "{\n  \"value\": \"ON\"\n}"

    headers = {
        'content-type': "application/json",
        'x-aio-key': "cc7c424522214ee6ae2106eebed45135"
        }

    conn.request("POST", "/api/v2/kvnkey/feeds/audio/data", payload, headers)

    #res = conn.getresponse()
    #data = res.read()

    print("Playing song!")
    #print(data.decode("utf-8"))
    print("\n")

def playoff():
    conn = http.client.HTTPSConnection("io.adafruit.com")

    payload = "{\n  \"value\": \"OFF\"\n}"

    headers = {
        'content-type': "application/json",
        'x-aio-key': "cc7c424522214ee6ae2106eebed45135"
        }

    conn.request("POST", "/api/v2/kvnkey/feeds/audio/data", payload, headers)

    #res = conn.getresponse()
    #data = res.read()

    print("Stopping song!")
    #print(data.decode("utf-8"))
    print("\n")

def playsong():

    if playnum == 0:
        pygame.mixer.music.play()
    elif playnum > 0:
        pygame.mixer.music.rewind()

while playnum < 81:
    playsong()
    blue()
    time.sleep(timez)
    yellow()
    time.sleep(timez)
    red()
    time.sleep(timez)
    green()
    time.sleep(timez)
    blue()
    time.sleep(timez)
    yellow()
    time.sleep(timez)
    green()
    time.sleep(timez)
    red()
    time.sleep(timez)
    blue()
    time.sleep(timez)
    yellow()
    time.sleep(timez)
    green()
    time.sleep(timez)
    playnum = playnum + 1
    print(playnum)
    print("\n")
