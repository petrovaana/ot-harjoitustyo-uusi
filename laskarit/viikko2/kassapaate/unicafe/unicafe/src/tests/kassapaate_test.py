import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate(100000)
    
    