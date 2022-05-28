from abc import ABC

from serviceable import Serviceable


class Car(Serviceable, ABC):
    def __init__(self, engine, battery):
        self.Engine = engine
        self.Battery = battery

    def needs_service(self):
        if self.Engine.needs_service() or self.Battery.needs_service():
            return True
        else:
            return False
