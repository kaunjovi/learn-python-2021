import unittest
from src.learn.unittest.HelloWorldUnittest import greet

class Test_HelloWorldUnittest(unittest.TestCase):
    def test_greet (self) : 
        self.assertEqual(greet(),'Hello world from Python unit test')