# ÖBB digital HV signal


## Description
This is an open-source project that provides detailed instructions for 
creating a 3D printed ÖBB (Austrian Federal Railways) signal model based 
on the [3d model](https://www.thingiverse.com/thing:6121234/files) of [Stubenflieger](https://www.thingiverse.com/stubenflieger/designs).

![signal photo](https://github.com/HeyJoFlyer/oebb-digital-scale-signal/signal.avif?raw=true "signal photo")

## Features
- 3D printed model
- Multicolor sign
- Based on the work of Stubenflieger
- All signal states implemented in software
- G-Scale model, also useable as decoration

## Requirements
To create the ÖBB signal, you will need:
1. A 3D printer with the appropriate capabilities (multicolor not required, but helps for `4_Hauptsignal_Platte multicolor.3mf`)
1. 12 5mm leds: (5 green, 3 yellow, 1 red, 3 white)
1. Raspberry Pi Pico with [Circuitpython](https://circuitpython.org/board/raspberry_pi_pico/) (no extra libraries)
1. Resistors and wires and 2 buttons


## Instructions
1. Print 3d models, you can choose to print 
1. if you dont have the required color or dont have a multicolor 3d printer, you should paint the parts (photos).
1. Under `test/code.py`you can find a test python script, where you will need to adjust the GP pins to your connected pins. With this script you can figure out which led is connected to which pin (took me ages without it), you can switch active led by pulling `GP0` low. You can view the output on the `REPL`using Thonny or MU editor.

## Acknowledgments
This open source project is based on the [work of Stubenflieger](https://www.thingiverse.com/thing:6121234/files).


## License
This project is licensed under the CC-BY-NC-4.0 License (as was Stubenfliegers design), following files are also available under the MIT License:
- `code.py`
- `test/cody.py``