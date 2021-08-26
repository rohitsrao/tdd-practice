import unittest

class BusDriver:

    def __init__(self, route):
        self.route = route
        self.gossip = ''
        self.gossip_received = []

class TestBusDriver(unittest.TestCase):

    def setUp(self):
        self.bus_driver = BusDriver([1, 2, 3])
    
    def test_create_BusDriver_object(self):
        self.assertIsInstance(self.bus_driver, BusDriver)
    
    def test_BusDriver_instance_contains_route_attribute(self):
        self.assertTrue(hasattr(self.bus_driver, 'route'))

    def test_BusDriver_route_instance_is_a_list(self):
        self.assertIsInstance(self.bus_driver.route, list)

    def test_BusDriver_route_is_not_empty(self):
        self.assertNotEqual(len(self.bus_driver.route), 0)

    def test_BusDriver_instance_contains_gossip_attribute(self):
        self.assertTrue(hasattr(self.bus_driver, 'gossip'))

    def test_BusDriver_gossip_is_string(self):
        self.assertIsInstance(self.bus_driver.gossip, str)

    def test_BusDriver_instance_contains_gossip_received_attribute(self):
        self.assertTrue(hasattr(self.bus_driver, 'gossip_received'))

    def test_BusDriver_gossip_heard_is_a_list(self):
        self.assertIsInstance(self.bus_driver.gossip_received, list)

    def test_BusDriver_gossip_heard_is_empty(self):
        self.assertTrue(not self.bus_driver.gossip_received)

if __name__ == '__main__':
    unittest.main()
