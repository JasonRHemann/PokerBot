import pyautogui
import threading


# x = pyautogui.locateOnScreen(
#     'images/button.png', confidence=.09, region=(106, 289, 441, 261))
# print(x)

im = pyautogui.screenshot()

dealer = im.getpixel((388, 508))
dealer1 = im.getpixel((156, 515))
dealer2 = im.getpixel((156, 363))
dealer3 = im.getpixel((407, 305))
dealer4 = im.getpixel((529, 363))
dealer5 = im.getpixel((529, 515))

print('me', dealer)
print(dealer1)
print(dealer2)
print(dealer3)
print(dealer4)
print(dealer5)
