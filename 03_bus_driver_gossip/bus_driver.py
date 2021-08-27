class BusDriver:

    def __init__(self, route):
        self.route = route
        self.gossip = ''
        self.gossip_received = []
        self.current_route_index = 0
        self.current_stop = self.route[0]
    
    def update_stop(self):
        if self.current_route_index == len(self.route) - 1:
            self.current_route_index = 0
        else:
            self.current_route_index += 1
        self.current_stop = self.route[self.current_route_index]

