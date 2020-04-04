from device_name import parse_device_name
import unittest

class NamesTestCase(unittest.TestCase):

    def test_parse_device_full_name_(self):
        result = parse_device_name("Cisco","Router","2911","Sec")
        self.assertEqual(result,"Cisco Router 2911 Sec")

if __name__=="__main__":
    unittest.main()
    

"""
    def test_parse_device_name(self):
        result = parse_device_name("Cisco","Router","2911")
        self.assertEqual(result,"Cisco Router 2911")
"""
