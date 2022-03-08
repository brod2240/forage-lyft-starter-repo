from abc import ABC

from engine import Engine


class CapuletEngine(Engine, ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date: last_service_date
        self.current_date: current_date

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > 30000:
            return True
        else:
            return False
