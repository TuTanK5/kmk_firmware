import board
from storage import getmount

import km
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.scanners import DiodeOrientation

split_side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT


class KMKKeyboard(_KMKKeyboard):
    # Keyboard wiring config
    col_pins = (board.P0_10,)
    row_pins = (board.P0_09,)
    diode_orientation = DiodeOrientation.COL2ROW

    # Modules
    layer_mod = Layers()
    # split = Split(split_type=SplitType.BLE, split_side=split_side)
    split_mod = Split(split_type=SplitType.BLE)

    modules = [split_mod, layer_mod]

    # Keymap
    coord_mapping = [0, 1]
    keymap = km.keymap

