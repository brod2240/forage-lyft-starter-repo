from abc import ABC
from tire import Tires
from numpy import np


class Octoprime(Tires, ABC):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        if np.sum(self.sensors) >= 3:
            return True
        else:
            return False
