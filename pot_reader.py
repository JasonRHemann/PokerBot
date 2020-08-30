from PIL import Image
import pytesseract as tessaract
import cv2
import pyautogui
tessaract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Pot location for 6 handed game APP
#pot_location = (291, 275, 100, 40)

# Pot location for 6 handed game WEB
pot_location = (291, 344, 100, 40)


def pot_reader():

    img = pyautogui.screenshot(region=pot_location)
    # img = Image.open("test9.png")
    new_size = tuple(3*x for x in img.size)
    img = img.resize(new_size, Image.ANTIALIAS)

    pot = tessaract.image_to_string(img)

    print(pot)


pot_reader()
