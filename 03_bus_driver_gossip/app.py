class App:
    
    def __init__(self, list_of_drivers):
        self.list_of_drivers = list_of_drivers
        self.timestep = 0
    
    def increment_timestep(self):
        self.timestep += 1

    def initialize_driver_gossip(self):
        for i in range(len(self.list_of_drivers)):
            driver = self.list_of_drivers[i]
            driver.gossip = 'g'+str(i)
    
    def generate_stop_list(self):
        route_concatenation = []
        for driver in self.list_of_drivers:
            route_concatenation += driver.route
        self.stops = set(route_concatenation)
    
    def update_all_driver_stops(self):
        for driver in self.list_of_drivers:
            driver.update_stop()
