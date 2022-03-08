from car import Car


class CarFactory(Car):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date: current_date
        self.last_service_date: last_service_date
        self.current_mileage: current_mileage
        self.last_service_date: last_service_mileage

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date: current_date
        self.last_service_date: last_service_date
        self.current_mileage: current_mileage
        self.last_service_date: last_service_mileage

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        self.current_date: current_date
        self.last_service_date: last_service_date
        self.warning_light_on: warning_light_on

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date: current_date
        self.last_service_date: last_service_date
        self.current_mileage: current_mileage
        self.last_service_date: last_service_mileage

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date: current_date
        self.last_service_date: last_service_date
        self.current_mileage: current_mileage
        self.last_service_date: last_service_mileage

