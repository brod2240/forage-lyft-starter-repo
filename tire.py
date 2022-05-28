from abc import ABC, abstractmethod


class Tires(ABC):
    def __init__(self, sensors):
        self.sensors = sensors

    @abstractmethod
    def needs_service(self):
        pass
