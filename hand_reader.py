import pyautogui
import time
import threading


player_card_one = ["Not Found", "Not Found"]
player_card_two = ["Not Found", "Not Found"]

# Card Location for 6 handed game APP
# card_location = (300, 420, 100, 75)

# Card Location for 6 handed game WEB
#card_location = (300, 505, 80, 43)

# Card Location for 9 handed game WEB
#card_location = (300, 505, 80, 43)

# Card Location for 6 handed game Laptop
card_location = (360, 545, 70, 50)

# Middle point for determining which card desktop
#middle = 340

# Middle point for determining which card laptop
middle = 393

# Lower or confidence if images are not found
confidence_scale = .8


def hand_reader():

    # threading.Timer(10.0, hand_reader).start()

    coordinates = pyautogui.locateAllOnScreen(
        'images/club.png', confidence=confidence_scale, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[1] = "of Clubs"
        if(element != None and element[0] > middle):
            player_card_two[1] = "of Clubs"

    coordinates = pyautogui.locateAllOnScreen(
        'images/spade.png', confidence=confidence_scale, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[1] = "of Spades"
        if(element != None and element[0] > middle):
            player_card_two[1] = "of Spades"

    coordinates = pyautogui.locateAllOnScreen(
        'images/diamond.png', confidence=confidence_scale, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[1] = "of Diamonds"
        if(element != None and element[0] > middle):
            player_card_two[1] = "of Diamonds"

    coordinates = pyautogui.locateAllOnScreen(
        'images/heart.png', confidence=confidence_scale, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[1] = "of Hearts"
        if(element != None and element[0] > middle):
            player_card_two[1] = "of Hearts"

    coordinates = pyautogui.locateAllOnScreen(
        'images/two.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Two"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Two"

    coordinates = pyautogui.locateAllOnScreen(
        'images/three.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Three"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Three"

    coordinates = pyautogui.locateAllOnScreen(
        'images/four.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Four"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Four"

    coordinates = pyautogui.locateAllOnScreen(
        'images/five.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Five"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Five"

    coordinates = pyautogui.locateAllOnScreen(
        'images/six.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Six"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Six"

    coordinates = pyautogui.locateAllOnScreen(
        'images/seven.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Seven"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Seven"

    coordinates = pyautogui.locateAllOnScreen(
        'images/eight.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Eight"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Eight"

    coordinates = pyautogui.locateAllOnScreen(
        'images/nine.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Nine"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Nine"

    coordinates = pyautogui.locateAllOnScreen(
        'images/ten.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Ten"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Ten"

    coordinates = pyautogui.locateAllOnScreen(
        'images/jack.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Jack"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Jack"

    coordinates = pyautogui.locateAllOnScreen(
        'images/queen.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Queen"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Queen"

    coordinates = pyautogui.locateAllOnScreen(
        'images/king.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "King"
        if(element != None and element[0] > middle):
            player_card_two[0] = "King"

    coordinates = pyautogui.locateAllOnScreen(
        'images/ace.png', confidence=confidence_scale, grayscale=True, region=card_location)
    for element in coordinates:
        if(element != None and element[0] < middle):
            player_card_one[0] = "Ace"
        if(element != None and element[0] > middle):
            player_card_two[0] = "Ace"

    print("Card 1: " + player_card_one[0] + " " + player_card_one[1])
    print("Card 2: " + player_card_two[0] + " " + player_card_two[1])


hand_reader()
