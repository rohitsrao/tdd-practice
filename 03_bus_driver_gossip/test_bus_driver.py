import unittest

from bus_driver import BusDriver

class TestBusDriver(unittest.TestCase):

    def setUp(self):
        self.route = [1, 2, 3]
        self.bus_driver = BusDriver(self.route)
    
    def test_create_BusDriver_object(self):
        self.assertIsInstance(self.bus_driver, BusDriver)
    
    def test_instance_contains_route_attribute(self):
        self.assertTrue(hasattr(self.bus_driver, 'route'))
        self.assertIsInstance(self.bus_driver.route, list)
        self.assertNotEqual(len(self.bus_driver.route), 0)
    
    def test_instance_contains_gossip_attribute(self):
        self.assertTrue(hasattr(self.bus_driver, 'gossip'))
        self.assertIsInstance(self.bus_driver.gossip, str)
    
    def test_instance_contains_gossip_received_attribute(self):
        self.assertTrue(hasattr(self.bus_driver, 'gossip_received'))
        self.assertIsInstance(self.bus_driver.gossip_received, list)
        self.assertTrue(not self.bus_driver.gossip_received)
    
    def test_has_current_position_attribute(self):
        self.assertTrue(hasattr(self.bus_driver, 'current_pos'))
        self.assertIsInstance(self.bus_driver.current_pos, int)
        self.assertEqual(self.bus_driver.current_pos, 0)
    
    def test_start_method_sets_current_position_to_first_entry_in_route(self):
        self.bus_driver.start()
        self.assertEqual(self.bus_driver.current_pos, self.route[0])


if __name__ == '__main__':
    unittest.main()
