import logging
import os
import sys

import conf
import layouts
from hk import HK

logging.basicConfig(level=logging.INFO)
import typing

from pynput import keyboard
from pynput.keyboard import Key, KeyCode

config = conf.load()
logging.info("Number of layouts: {}".format(layouts.get_count()))
logging.info("Config: {}".format(config))
logging.info("Variants: {}".format(layouts.get_variants_filtered()))
sys.exit()
def left():
    layouts.right()

def right():
    layouts.left()

hotkeys:typing.List[HK] = [
    HK([Key.ctrl, Key.shift], left),
    HK([Key.ctrl_r, Key.shift_r], right)
]

_keymap = {
    65511: Key.alt,
    65512: Key.alt_r,
    65034: Key.ctrl,
    65032: Key.ctrl_r
}
def mapper(key):
    logging.info("type: {} key: {}".format(type(key), key))
    if isinstance(key, KeyCode) and key.vk in _keymap:
        return _keymap[key.vk]
    return key


def press(key):
    key = mapper(key)
    print("Pressed: {}".format(key))
    for k in hotkeys:
        k.press(key)

def release(key):
    key = mapper(key)
    print("Release: {}".format(key))
    for k in hotkeys:
        k.release(key)

with keyboard.Listener(
        on_press=press,
        on_release=release) as l:
    l.join()
