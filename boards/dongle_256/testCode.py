import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes

print('Starting')

keyboard = KMKKeyboard()

keyboard.col_pins = (board.P0_09,)
keyboard.row_pins = (board.P0_10,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A,]
]
if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='dongle256')
