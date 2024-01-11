import unittest
from package_test_squab77.package_test_squab77 import awesome_test

class TestStuff(unittest.TestCase):

  def test_thing(self):
    """Test thing"""
    try:
      awesome_test()
    except Exception:
      self.fail('thing failed')