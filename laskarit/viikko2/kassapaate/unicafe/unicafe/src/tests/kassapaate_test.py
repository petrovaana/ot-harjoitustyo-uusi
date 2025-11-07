import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_kassassa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_oikeat_edullisten_maarat(self):
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_oikeat_maukkauiden_maarat(self):
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_oikea_vaihto_raha_edullisilla(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(400)
        self.assertEqual(vaihtoraha, 160)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    
    def test_oikea_vaihto_raha_maukkailla(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_liian_vahan_rahaa_edullisilla(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_liian_vahan_rahaa_maukkailla(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_maksukortti_edulliset(self):
        maksu = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(maksu)
        self.assertEqual(self.kortti.saldo, 760)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maksukortti_edulliset_liian_vahan_rahaa(self):
        self.kortti = Maksukortti(100)
        maksu = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertFalse(maksu)
        self.assertEqual(self.kortti.saldo, 100)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_maksukortti_maukkaat(self):
        maksu = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(maksu)
        self.assertEqual(self.kortti.saldo, 600)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maksukortti_maukkaat_liian_vahan_rahaa(self):
        self.kortti = Maksukortti(100)
        maksu = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertFalse(maksu)
        self.assertEqual(self.kortti.saldo, 100)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_maksukortille_rahan_lataaminen(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo_euroina(), 11.0)

    def test_maksukortille_negatiivisen_maaran_lataaminen(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)
    
    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)