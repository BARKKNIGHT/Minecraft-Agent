import pydirectinput
import time

class Controller:
    def __init__(self):
        self.current_keys = set()

    def press_key(self, key):
        if key not in self.current_keys:
            pydirectinput.keyDown(key)
            self.current_keys.add(key)

    def release_key(self, key):
        if key in self.current_keys:
            pydirectinput.keyUp(key)
            self.current_keys.remove(key)

    def release_all(self):
        for key in list(self.current_keys):
            self.release_key(key)
    
    def map_steering(value):
        if value < -0.5:
            return 'a'  # Turn left
        elif value > 0.5:
            return 'd'  # Turn right
        else:
            return None  # Go straight

    def map_throttle(value):
        if value > 0.5:
            return 'w'  # Accelerate
        else:
            return 's'  # Brake



# Example Usage
# controller = Controller()
# time.sleep(5)
# controller.press_key('w')  # Accelerate
# time.sleep(1)
# controller.release_key('w')  # Stop accelerating

