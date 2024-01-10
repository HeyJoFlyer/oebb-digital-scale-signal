# SPDX-FileCopyrightText: 2024 Nico Gartner
#
# SPDX-License-Identifier: MIT
import board
import time
from digitalio import DigitalInOut, Direction, Pull

led1 = DigitalInOut(board.GP14)
led2 = DigitalInOut(board.GP21)
led3 = DigitalInOut(board.GP18)
led4 = DigitalInOut(board.GP22)

led5 = DigitalInOut(board.GP26)
led6 = DigitalInOut(board.GP13)
led7 = DigitalInOut(board.GP12)
led8 = DigitalInOut(board.GP20)
led9 = DigitalInOut(board.GP19)
led10 = DigitalInOut(board.GP15)
led11 = DigitalInOut(board.GP17)
led12 = DigitalInOut(board.GP16)

led1.direction = Direction.OUTPUT
led2.direction = Direction.OUTPUT
led3.direction = Direction.OUTPUT
led4.direction = Direction.OUTPUT

led5.direction = Direction.OUTPUT
led6.direction = Direction.OUTPUT
led7.direction = Direction.OUTPUT
led9.direction = Direction.OUTPUT
led9.direction = Direction.OUTPUT
led10.direction = Direction.OUTPUT
led11.direction = Direction.OUTPUT
led12.direction = Direction.OUTPUT

button = DigitalInOut(board.GP0)
button.direction = Direction.INPUT
button.pull = Pull.UP
old_time = time.time()

pins = []
for i in range(12):
    pins.append(f"led{i + 1}")
index = 0

while True:
    if button.value == True and time.time() - old_time > 1:
        old_time = time.time()
        index += 1
        if index > len(pins) - 1:
            index = 0
        print(pins[index])
        if pins[index] == "led1":
            led1.value = True
        else:
            led1.value = False
        if pins[index] == "led2":
            led2.value = True
        else:
            led2.value = False
        if pins[index] == "led3":
            led3.value = True
        else:
            led3.value = False
        if pins[index] == "led4":
            led4.value = True
        else:
            led4.value = False
        if pins[index] == "led5":
            led5.value = True
        else:
            led5.value = False
        if pins[index] == "led6":
            led6.value = True
        else:
            led6.value = False
        if pins[index] == "led7":
            led7.value = True
        else:
            led7.value = False
        if pins[index] == "led8":
            led8.value = True
        else:
            led8.value = False
        if pins[index] == "led9":
            led9.value = True
        else:
            led9.value = False
        if pins[index] == "led10":
            led10.value = True
        else:
            led10.value = False
        if pins[index] == "led11":
            led11.value = True
        else:
            led11.value = False
        if pins[index] == "led12":
            led12.value = True
        else:
            led12.value = False
