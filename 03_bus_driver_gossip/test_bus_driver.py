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
    
    def test_has_current_route_index_attribute(self):
        self.assertTrue(hasattr(self.bus_driver, 'current_route_index'))
        self.assertIsInstance(self.bus_driver.current_route_index, int)
        self.assertEqual(self.bus_driver.current_route_index, 0)

    def test_has_current_stop_attribute(self):
        self.assertTrue(hasattr(self.bus_driver, 'current_stop'))
        self.assertIsInstance(self.bus_driver.current_stop, int)
        self.assertEqual(self.bus_driver.current_stop, self.route[0])
    
    def test_update_stop_changes_current_stop_to_next_in_route(self):
        self.bus_driver.update_stop()
        self.assertEqual(self.bus_driver.current_stop, self.route[1])

    def test_running_update_stop_twice_changes_stop_to_3rd_in_route(self):
        self.bus_driver.update_stop()
        self.bus_driver.update_stop()
        self.assertEqual(self.bus_driver.current_stop, self.route[2])

    def test_running_update_stop_more_than_length_of_routes_resets_to_first_stop(self):
        self.bus_driver.update_stop()
        self.bus_driver.update_stop()
        self.bus_driver.update_stop()
        self.assertEqual(self.bus_driver.current_stop, self.route[0])



if __name__ == '__main__':
    unittest.main()
