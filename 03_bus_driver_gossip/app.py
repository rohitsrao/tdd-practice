class App:
    
    def __init__(self, list_of_drivers):
        self.list_of_drivers = list_of_drivers
        self.timestep = 0
        self.generate_stop_list()
        self.generate_drivers_per_stop()

    def count_driver_per_stop(self):
        for stop in self.stops:
            self.drivers_at_stop[stop] = [driver for driver in self.list_of_drivers if driver.current_stop == stop]

    def increment_timestep(self):
        self.timestep += 1

    def initialize_driver_gossip(self):
        for i in range(len(self.list_of_drivers)):
            driver = self.list_of_drivers[i]
            driver.gossip = 'g'+str(i)
            driver.gossip_received.append(driver.gossip)

    def generate_drivers_per_stop(self):
        self.drivers_at_stop = {}
        for stop in self.stops:
            self.drivers_at_stop[stop] = []

    def generate_stop_list(self):
        route_concatenation = []
        for driver in self.list_of_drivers:
            route_concatenation += driver.route
        self.stops = set(route_concatenation)
    
    def update_all_driver_stops(self):
        for driver in self.list_of_drivers:
            driver.update_stop()
