class BusDriver:

    def __init__(self, route):
        self.route = route
        self.gossip = ''
        self.gossip_received = []
        self.current_pos = 0

    def start(self):
        self.current_pos = self.route[0]

