class App:
    
    def __init__(self, list_of_drivers):
        self.list_of_drivers = list_of_drivers
        self.timestep = 0

    def initialize_drivers(self):
        for driver in self.list_of_drivers:
            driver.start()

    def generate_stop_list(self):
        route_concatenation = []
        for driver in self.list_of_drivers:
            route_concatenation += driver.route
        self.stops = set(route_concatenation)

