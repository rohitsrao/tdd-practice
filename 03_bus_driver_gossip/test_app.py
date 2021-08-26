import unittest 

from bus_driver import BusDriver
from app import App

class TestApp(unittest.TestCase):

    def setUp(self):
        bus_driver_1 = BusDriver([3, 1, 2, 3])
        bus_driver_2 = BusDriver([3, 2, 3, 1])
        bus_driver_3 = BusDriver([4, 2, 3, 4, 5])
        self.app = App([bus_driver_1, bus_driver_2, bus_driver_3])
    
    def test_create_App_instance(self):
        self.assertIsInstance(self.app, App)

    def test_App_has_list_of_drivers_attribute(self):
        self.assertTrue(hasattr(self.app, 'list_of_drivers'))

    def test_App_list_of_drivers_is_list(self):
        self.assertIsInstance(self.app.list_of_drivers, list)

if __name__ == '__main__':
    unittest.main()
