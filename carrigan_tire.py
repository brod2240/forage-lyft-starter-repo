from abc import ABC
from tire import Tires


class Carrigan(Tires, ABC):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        for x in self.sensors:
            if x >= 0.9:
                return True
            else:
                return False
