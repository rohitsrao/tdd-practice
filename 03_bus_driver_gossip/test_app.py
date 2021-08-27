import unittest 

from bus_driver import BusDriver
from app import App

class TestApp(unittest.TestCase):

    def setUp(self):
        self.bus_driver_0 = BusDriver([3, 1, 2, 3])
        self.bus_driver_1 = BusDriver([3, 2, 3, 1])
        self.bus_driver_2 = BusDriver([4, 2, 3, 4, 5])
        self.list_of_drivers = [self.bus_driver_0, self.bus_driver_1, self.bus_driver_2]
        self.app = App(self.list_of_drivers)
    
    def test_create_App_instance(self):
        self.assertIsInstance(self.app, App)
    
    def test_list_of_drivers_attribute(self):
        self.assertTrue(hasattr(self.app, 'list_of_drivers'))
        self.assertIsInstance(self.app.list_of_drivers, list)
    
    def test_timestep_attribute(self):
        self.assertTrue(hasattr(self.app, 'timestep'))
        self.assertEqual(self.app.timestep, 0)
    
    def test_calling_generate_stop_set_creates_non_empty_set_attribute_stops(self):
        self.app.generate_stop_list()
        self.assertIsInstance(self.app.stops, set)
        self.assertNotEqual(len(self.app.stops), 0)

    def test_calling_increment_timestep_updates_timestep(self):
        self.app.increment_timestep()
        self.app.increment_timestep()
        self.assertEqual(self.app.timestep, 2)

    def test_calling_update_all_driver_stops(self):
        self.app.update_all_driver_stops()
        for driver in self.list_of_drivers:
            self.assertEqual(driver.current_stop, driver.route[1])

    def test_initialize_driver_gossip_sets_driver_gossip_to_g_index(self):
        self.app.initialize_driver_gossip()
        for i in range(len(self.list_of_drivers)):
            driver = self.list_of_drivers[i]
            self.assertEqual(driver.gossip, 'g'+str(i))
            self.assertEqual(driver.gossip_received, ['g'+str(i)])


if __name__ == '__main__':
    unittest.main()
