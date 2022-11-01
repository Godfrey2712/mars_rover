import unittest
from mars_rover import robot

class MarsRoverTest(unittest.TestCase):

       def test_rover(self):
              self.assertEqual(robot(), ('OUTPUT:', 1, 4, 'W'))
if __name__ == '__main__':
    unittest.main()