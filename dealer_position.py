import pyautogui
import threading
import time

# Dealer positions for 6 handed desktop
dealer_position1 = (388, 508)
dealer_position2 = (156, 515)
dealer_position3 = (156, 363)
dealer_position4 = (407, 305)
dealer_position5 = (529, 363)
dealer_position6 = (529, 515)

# Dealer postions for 6 handed laptop
# dealer_position1 = (442, 552)
# dealer_position2 = (220, 559)
# dealer_position3 = (220, 413)
# dealer_position4 = (460, 358)
# dealer_position5 = (576, 413)
# dealer_position6 = (576, 559)

dealer_list = [dealer_position1, dealer_position2, dealer_position3,
               dealer_position4, dealer_position5, dealer_position6]

# threading.Timer(5.0, dealer_seat).start()


# class Dealer:

#     def __init__(self, seat):
#         self.seat = seat
#         self.greeting = "The dealer is in seat {}".format(seat)

#     def __repr__(self):
#         return "dealer is in seat {}".format(self.seat)


# dealer = Dealer(4)
# print(dealer)


# class Dealer:
#     def __init__(self, seat):
#         self.seat = seat

#     def __repr__(self):
#         return "Dealer is in seat {}".format(self.seat)

#     def dealer_seat():

#         # threading.Timer(5.0, dealer_seat).start()

#         for idx, val in enumerate(dealer_list):
#             im = pyautogui.screenshot()
#             button = im.getpixel(val)
#             if(button[0] > 200):
#                 dealer = idx
#                 print(dealer)

#     dealer_seat()
# class Watcher:
#     def __init__(self, value):
#         self.variable = value

#     def set_value(self, new_value):
#         if self.value != new_value:
#             self.pre_change()
#             self.variable = new_value
#             self.post_change()

#     def pre_change(self):
#         print(value)

#     def post_change(self):
#         print(value)


# class Employee:

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)


# emp_1 = Employee("Jason", "Hemann")

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())

# def dealer_seat():

#     threading.Timer(5.0, dealer_seat).start()

#     for idx, val in enumerate(dealer_list):
#         im = pyautogui.screenshot()
#         button = im.getpixel(val)
#         if(button[0] > 200):
#             dealer = idx
#             print(dealer)


# dealer_seat()
