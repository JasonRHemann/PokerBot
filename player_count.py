import pyautogui
import threading
import time

# Player seats for 6 handed desktop WEB
player_seat1 = ()
player_seat2 = ()
player_seat3 = ()
player_seat4 = ()
player_seat5 = ()
player_seat6 = ()

seat_list = [player_seat1, player_seat2, player_seat3,
             player_seat4, player_seat5, player_seat6]


def player_count():

    threading.Timer(5.0, player_count).start()

    for idx, val in enumerate(seat_list):
        im = pyautogui.screenshot()
        button = im.getpixel(val)
        if(button[0] > 200):
            players = idx
            print(players)


player_count()
