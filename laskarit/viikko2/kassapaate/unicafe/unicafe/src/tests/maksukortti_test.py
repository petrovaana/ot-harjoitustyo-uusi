import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kortille(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)
    
    def test_saldon_vaheneminen_kun_on_rahaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5)

    def test_negatiivinen_summa_ei_muuta_saldoa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(100))

    def test_negatiivinen_summa_ei_muuta_saldoa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(2000))
    
    def test_str(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")