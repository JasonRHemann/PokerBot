import pyautogui
import time

# time.sleep(1)
# print(pyautogui.locateOnScreen('12C.png', region=(306, 433, 65, 43)))

player_card_one = [0, 0]
player_card_two = [0, 0]

coordinates = pyautogui.locateAllOnScreen('club.png', confidence=.9)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[1] = "of Clubs"
    if(element != None and element[0] > 340):
        player_card_two[1] = "of Clubs"


coordinates = pyautogui.locateAllOnScreen('spade.png', confidence=.9)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[1] = "of Spades"
    if(element != None and element[0] > 340):
        player_card_two[1] = "of Spades"

coordinates = pyautogui.locateAllOnScreen('diamond.png', confidence=.9)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[1] = "of Diamonds"
    if(element != None and element[0] > 340):
        player_card_two[1] = "of Diamonds"

coordinates = pyautogui.locateAllOnScreen('heart.png', confidence=.9)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[1] = "of Hearts"
    if(element != None and element[0] > 340):
        player_card_two[1] = "of Hearts"

coordinates = pyautogui.locateAllOnScreen(
    'two.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Two"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Two"

coordinates = pyautogui.locateAllOnScreen(
    'three.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Three"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Three"

coordinates = pyautogui.locateAllOnScreen(
    'four.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Four"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Four"

coordinates = pyautogui.locateAllOnScreen(
    'five.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Five"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Five"

coordinates = pyautogui.locateAllOnScreen(
    'six.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Six"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Six"

coordinates = pyautogui.locateAllOnScreen(
    'seven.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Seven"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Seven"

coordinates = pyautogui.locateAllOnScreen(
    'eight.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Eight"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Eight"

coordinates = pyautogui.locateAllOnScreen(
    'nine.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Nine"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Nine"

coordinates = pyautogui.locateAllOnScreen(
    'ten.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Ten"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Ten"

coordinates = pyautogui.locateAllOnScreen(
    'jack.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Jack"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Jack"

coordinates = pyautogui.locateAllOnScreen(
    'queen.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Queen"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Queen"

coordinates = pyautogui.locateAllOnScreen(
    'king.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "King"
    if(element != None and element[0] > 340):
        player_card_two[0] = "King"

coordinates = pyautogui.locateAllOnScreen(
    'ace.png', confidence=.9, grayscale=True)
for element in coordinates:
    if(element != None and element[0] < 340):
        player_card_one[0] = "Ace"
    if(element != None and element[0] > 340):
        player_card_two[0] = "Ace"

print("Card 1: " + player_card_one[0] + " " + player_card_one[1])
print("Card 2: " + player_card_two[0] + " " + player_card_two[1])
