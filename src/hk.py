import logging
import typing

from pynput.keyboard import Key


class HK:
    def __init__(self, keys: typing.List[Key], callback):
        self.keys = keys
        self.pressed = set()
        self.callback = callback


    def press(self, key):
        if key not in self.keys:
            self.pressed.clear()
        else:
            self.pressed.add(key)
    def _rem_key(self, key):
        if key in self.pressed:
            self.pressed.remove(key)

    def release(self, key):
        if key in self.keys:
            res = self.check()
            self._rem_key(key)
            #return not res
        else:
            self.pressed.clear()

    def check(self):
        logging.info("Checking: {} == {}".format(self.keys, self.pressed))
        if len(self.pressed) == len(self.keys):
            try:
                self.callback()
            except Exception as e:
                logging.error("Error in callback:", e)
            finally:
                return True
        return False