import unittest
import os
import sys
import code

class code_TestCase(unittest.TestCase):
  "TestCase class for find_package function"

  def setUp(self):
    pass

  def test_say_hello(self):
    val = code.say_hello()
    self.assertEqual(val, "Hello world")




if __name__ == "__main__":
  unittest.main()
