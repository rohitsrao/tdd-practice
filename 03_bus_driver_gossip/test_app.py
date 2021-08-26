import unittest 

from bus_driver import BusDriver
from app import App

class TestApp(unittest.TestCase):

    def setUp(self):
        self.bus_driver_1 = BusDriver([3, 1, 2, 3])
        self.bus_driver_2 = BusDriver([3, 2, 3, 1])
        self.bus_driver_3 = BusDriver([4, 2, 3, 4, 5])
        self.list_of_drivers = [self.bus_driver_1, self.bus_driver_2, self.bus_driver_3]
        self.app = App(self.list_of_drivers)
    
    def test_create_App_instance(self):
        self.assertIsInstance(self.app, App)
    
    def test_list_of_drivers_attribute(self):
        self.assertTrue(hasattr(self.app, 'list_of_drivers'))
        self.assertIsInstance(self.app.list_of_drivers, list)
    
    def test_initalize_drivers_method(self):
        self.assertTrue(hasattr(self.app, 'initialize_drivers'))
    
    def test_timestep_attribute(self):
        self.assertTrue(hasattr(self.app, 'timestep'))
        self.assertEqual(self.app.timestep, 0)
    
    def test_after_calling_initialize_drivers_current_pos_of_all_buses_updated(self):
        self.app.initialize_drivers()
        for bus_driver in self.list_of_drivers:
            self.assertEqual(bus_driver.current_pos, bus_driver.route[0])
    
    def test_calling_generate_stop_list_creates_non_empty_list_attribute_stops(self):
        self.app.generate_stop_list()
        self.assertIsInstance(self.app.stops, set)
        self.assertNotEqual(len(self.app.stops), 0)


if __name__ == '__main__':
    unittest.main()
