import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto( unittest.TestCase ):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento( self ):
        conjunto = Conjunto([5])
        self.assertEqual(5, conjunto.promedio())

    def test_conjunto_dosElemento_retornaPromedioElemento( self ):
        conjunto = Conjunto([5, 7])
        self.assertEqual(6, conjunto.promedio())

    def test_conjunto_nElemento_retornaPromedioNElemento( self ):
        conjunto = Conjunto([2, 4, 8, 9, 10, 15])
        self.assertEqual((2+4+8+9+10+15)/6, conjunto.promedio())