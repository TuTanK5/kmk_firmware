
from kb import KMKKeyboard
from kmk.hid import HIDModes
from kmk.modules.split import SplitSide

print('Starting')

keyboard = KMKKeyboard()

if __name__ == '__main__':
    if keyboard.side == SplitSide.LEFT:
        # Used left side to connect to PC, name your ble device with ble_name
        keyboard.go(hid_type=HIDModes.BLE, ble_name='dongle256')
    else:
        keyboard.go()
