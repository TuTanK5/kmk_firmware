import board

import km
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType
from storage import getmount


class KMKKeyboard(_KMKKeyboard):
    # Keyboard wiring config
    col_pins = (board.P0_31, board.P0_29, board.P0_02, board.P1_15, board.P1_13, board.P1_10,)
    row_pins = (board.P0_22, board.P0_24, board.P1_00, board.P0_09, board.P0_10,)
    diode_orientation = DiodeOrientation.ROW2COL

    # Modules
    layer_mod = Layers()
    # rename your drive https://learn.adafruit.com/welcome-to-circuitpython/renaming-circuitpy
    # where name should end with L or R
    side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
    split = Split(split_type=SplitType.BLE, split_side=side)

    modules = [layer_mod, split]

    # Keymap
    keymap = km.keymap

    debug_enabled = True
