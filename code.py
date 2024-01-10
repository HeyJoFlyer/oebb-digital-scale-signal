# SPDX-FileCopyrightText: 2024 Nico Gartner
#
# SPDX-License-Identifier: MIT
import board
import time
from digitalio import DigitalInOut, Direction, Pull

right_yellow_light = DigitalInOut(board.GP14)
left_yellow_light = DigitalInOut(board.GP12)
right_green_light = DigitalInOut(board.GP20)
left_green_light = DigitalInOut(board.GP18)

hp1_green_light = DigitalInOut(board.GP26)
hp2_green_light = DigitalInOut(board.GP13)
hp2_yellow_light = DigitalInOut(board.GP22)
hp0_red_light = DigitalInOut(board.GP17)
depature_green_light = DigitalInOut(board.GP19)
upper_white_light = DigitalInOut(board.GP15)
lower_white_light = DigitalInOut(board.GP21)
right_white_light = DigitalInOut(board.GP16)

right_yellow_light.direction = Direction.OUTPUT
left_yellow_light.direction = Direction.OUTPUT
right_green_light.direction = Direction.OUTPUT
left_green_light.direction = Direction.OUTPUT

hp1_green_light.direction = Direction.OUTPUT
hp2_green_light.direction = Direction.OUTPUT
hp2_yellow_light.direction = Direction.OUTPUT
hp0_red_light.direction = Direction.OUTPUT
depature_green_light.direction = Direction.OUTPUT
upper_white_light.direction = Direction.OUTPUT
lower_white_light.direction = Direction.OUTPUT
right_white_light.direction = Direction.OUTPUT

right_yellow_light.value = False
left_yellow_light.value = False
right_green_light.value = False
left_green_light.value = False

hp1_green_light.value = False
hp2_green_light.value = False
hp2_yellow_light.value = False
hp0_red_light.value = False
depature_green_light.value = False
upper_white_light.value = False
lower_white_light.value = False
right_white_light.value = False

button = DigitalInOut(board.GP0)
button.direction = Direction.INPUT
button.pull = Pull.UP

button_vor = DigitalInOut(board.GP1)
button_vor.direction = Direction.INPUT
button_vor.pull = Pull.UP

# (0, 0, 0, 0, 0, 0, 0, 0)
# (0, 0, 0, 0)

signalbegriffe = {"halt": (0, 0, 0, 1, 0, 0, 0, 0), "frei": (1, 0, 0, 0, 0, 0, 0, 0), "frei 60": (1, 1, 0, 0, 0, 0, 0, 0), "frei 40": (1, 0, 1, 0, 0, 0, 0, 0), "fahrverbot aufgehoben": (0, 0, 0, 0, 0, 1, 1, 0), "verschubverbot aufgehoben": (0, 0, 0, 1, 0, 0, 1, 1), "abfahren erlaubt": (1, 0, 0, 0, 2, 0, 0, 0), "ersatzsignal": (0, 0, 0, 1, 0, 2, 0, 0)}
vorsignalbegriffe = {"vorsicht": (1, 1, 0, 0), "hautpsignal frei": (0, 0, 1, 1), "hautpsignal frei 60": (0, 1, 1, 1), "hautpsignal frei 40": (1, 1, 0, 1), "abgeschaltet": (0, 0, 0, 0)}
signalbegriffe_keys = list(signalbegriffe.keys())
vorsignalbegriffe_keys = list(vorsignalbegriffe.keys())

def signal(signalbegriff_index, vorsignalbegriff_index):
    j = signalbegriffe_keys[signalbegriff_index]
    values = signalbegriffe[j]
    k = vorsignalbegriffe_keys[vorsignalbegriff_index]
    print(j, k)
    values_vor = vorsignalbegriffe[k]
    to_blink = []
    if values[0] == 1:
        hp1_green_light.value = True
    elif values[0] == 2:
        to_blink.append(hp1_green_light)
    else:
        hp1_green_light.value = False
    
    if values[1] == 1:
        hp2_green_light.value = True
    elif values[1] == 2:
        to_blink.append(hp2_green_light)
    else:
        hp2_green_light.value = False
    
    if values[2] == 1:
        hp2_yellow_light.value = True
    elif values[2] == 2:
        to_blink.append(hp2_yellow_light)
    else:
        hp2_yellow_light.value = False

    if values[3] == 1:
        hp0_red_light.value = True
    elif values[3] == 2:
        to_blink.append(hp0_red_light)
    else:
        hp0_red_light.value = False

    if values[4] == 1:
        depature_green_light.value = True
    elif values[4] == 2:
        to_blink.append(depature_green_light)
    else:
        depature_green_light.value = False

    if values[5] == 1:
        upper_white_light.value = True
    elif values[5] == 2:
        to_blink.append(upper_white_light)
    else:
        upper_white_light.value = False

    if values[6] == 1:
        lower_white_light.value = True
    elif values[6] == 2:
        to_blink.append(lower_white_light)
    else:
        lower_white_light.value = False

    if values[7] == 1:
        right_white_light.value = True
    elif values[7] == 2:
        to_blink.append(right_white_light)
    else:
        right_white_light.value = False

    if values_vor[0] == 1:
        right_yellow_light.value = True
    elif values_vor[0] == 2:
        to_blink.append(right_yellow_light)
    else:
        right_yellow_light.value = False

    if values_vor[1] == 1:
        left_yellow_light.value = True
    elif values_vor[1] == 2:
        to_blink.append(left_yellow_light)
    else:
        left_yellow_light.value = False

    if values_vor[2] == 1:
        right_green_light.value = True
    elif values_vor[2] == 2:
        to_blink.append(right_green_light)
    else:
       right_green_light.value = False

    if values_vor[3] == 1:
        left_green_light.value = True
    elif values_vor[3] == 2:
        to_blink.append(left_green_light)
    else:
        left_green_light.value = False
    return to_blink

old_time = time.time()
old_time_vor = time.time()
old_animation_time = time.time()
signalbegriffe_index = 0
vorsignalbegriffe_index = 0
animation_list = []
on = False

signal(signalbegriffe_index, vorsignalbegriffe_index)

while True:
    time.sleep(0.01)
    if button.value == False and time.time() - old_time > 0.4:
        old_time = time.time()
        signalbegriffe_index += 1
        if signalbegriffe_index > len(signalbegriffe) - 1:
            signalbegriffe_index = 0
        animation_list = signal(signalbegriffe_index, vorsignalbegriffe_index)

    if button_vor.value == False and time.time() - old_time_vor > 0.4:
        old_time_vor = time.time()
        vorsignalbegriffe_index += 1
        if vorsignalbegriffe_index > len(vorsignalbegriffe) - 1:
            vorsignalbegriffe_index = 0
        animation_list = signal(signalbegriffe_index, vorsignalbegriffe_index)   

    if time.time() - old_animation_time > 1:
        old_animation_time = time.time()
        for light in animation_list:
            light.value = on
        on = not on
